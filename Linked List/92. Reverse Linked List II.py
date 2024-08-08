# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist from `left` to `right`
        current = prev.next
        next_node = None
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next

# Example usage:
# Constructing the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
left = 2
right = 4
new_head = solution.reverseBetween(head, left, right)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [1, 4, 3, 2, 5]

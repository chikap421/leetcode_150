# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current, prev, next = head, dummy, None
        
        # First, count the length of the linked list
        length = 0
        while current:
            length += 1
            current = current.next

        # Loop over the list and reverse each k-group
        while length >= k:
            current = prev.next
            next = current.next
            for _ in range(1, k):
                current.next = next.next
                next.next = prev.next
                prev.next = next
                next = current.next
            prev = current
            length -= k

        return dummy.next

# Example usage:
# Constructing the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
k = 2
new_head = solution.reverseKGroup(head, k)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [2, 1, 4, 3, 5]

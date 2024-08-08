# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        second.next = second.next.next
        
        return dummy.next

# Example usage:
# Constructing the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
n = 2
new_head = solution.removeNthFromEnd(head, n)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [1, 2, 3, 5]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Initialize two dummy nodes
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Initialize pointers for the two lists
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect the two lists
        greater.next = None  # Ensure the last node of the greater list points to None
        less.next = greater_head.next  # Connect the less list to the greater list
        
        return less_head.next

# Example usage:
# Constructing the linked list [1, 4, 3, 2, 5, 2]
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

solution = Solution()
new_head = solution.partition(head, 3)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [1, 2, 2, 4, 3, 5]

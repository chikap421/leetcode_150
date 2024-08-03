# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Connect the last node to the head to form a circle
        tail.next = head
        
        # Step 3: Calculate the effective rotations needed
        k = k % length
        steps_to_new_tail = length - k
        
        # Step 4: Find the new tail and new head
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Step 5: Break the circle
        new_tail.next = None
        
        return new_head

# Example usage:
# Constructing the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.rotateRight(head, 2)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [4, 5, 1, 2, 3]

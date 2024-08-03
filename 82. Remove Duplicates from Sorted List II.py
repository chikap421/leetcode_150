# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            # Check if current node is a duplicate
            is_duplicate = False
            while current.next and current.val == current.next.val:
                current = current.next
                is_duplicate = True
            
            # If duplicates were found, skip them
            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next
            
            current = current.next
        
        return dummy.next

# Example usage:
# Constructing the linked list [1,2,3,3,4,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.deleteDuplicates(head)

# Output the result linked list
output = []
current = new_head
while current:
    output.append(current.val)
    current = current.next
print(output)  # Output should be [1, 2, 5]

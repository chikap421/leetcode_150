# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If we reach the end of one list, append the other list
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next

# Example usage:
# Creating first linked list 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Creating second linked list 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.mergeTwoLists(l1, l2)

# Output the result linked list
output = []
while result is not None:
    output.append(result.val)
    result = result.next
print(output)  # Output: [1, 1, 2, 3, 4, 4]

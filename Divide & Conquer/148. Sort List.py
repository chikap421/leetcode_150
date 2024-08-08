# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # Helper function to merge two sorted lists
        def merge(l1, l2):
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1:
                current.next = l1
            if l2:
                current.next = l2
            return dummy.next
        
        # Helper function to find the middle of the list
        def get_middle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Find the middle of the list
        middle = get_middle(head)
        right_head = middle.next
        middle.next = None
        
        # Sort each half
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        # Merge sorted halves
        return merge(left, right)

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Create a min-heap
        min_heap = []
        
        # Initialize the heap with the head of each list
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, l))
        
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        current = dummy
        
        # While there are nodes in the heap
        while min_heap:
            # Pop the smallest node from the heap
            val, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            
            # If there is a next node in the list, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next

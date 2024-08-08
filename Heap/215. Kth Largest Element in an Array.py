import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a min-heap with the first k elements from nums
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate over the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        # The root of the heap is the kth largest element
        return min_heap[0]

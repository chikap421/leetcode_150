import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        # Handle edge cases
        if not nums1 or not nums2 or k <= 0:
            return []

        # Min-heap to store the pairs and their sums
        min_heap = []
        
        # Initialize the heap with pairs from nums1[0] and all elements in nums2
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        result = []
        
        # Extract the smallest pairs
        while k > 0 and min_heap:
            sum_, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there are more elements in nums1 to consider
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            k -= 1
        
        return result

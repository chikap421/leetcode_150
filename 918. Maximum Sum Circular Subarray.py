class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        total_sum = sum(nums)
        max_kadane = kadane(nums)
        min_kadane = kadane([-x for x in nums])
        max_circular = total_sum + min_kadane
        
        if max_circular == 0:
            return max_kadane
        return max(max_kadane, max_circular)

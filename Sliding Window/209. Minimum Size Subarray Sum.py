class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum_ = 0
        min_length = float('inf')
        
        for end in range(len(nums)):
            sum_ += nums[end]
            
            while sum_ >= target:
                min_length = min(min_length, end - start + 1)
                sum_ -= nums[start]
                start += 1
        
        return 0 if min_length == float('inf') else min_length

# Example usage
solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Output: 2
print(solution.minSubArrayLen(4, [1, 4, 4]))           # Output: 1
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0

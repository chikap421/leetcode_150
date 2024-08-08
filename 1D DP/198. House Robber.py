class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the base cases
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            # Calculate the maximum amount of money we can rob up to the current house
            current = max(prev1, prev2 + num)
            # Update prev1 and prev2 for the next iteration
            prev2 = prev1
            prev1 = current
        
        return prev1

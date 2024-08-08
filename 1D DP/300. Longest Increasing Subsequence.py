class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left

        if not nums:
            return 0

        # dp will hold the smallest tail value of all increasing subsequences with length i+1
        dp = []

        for num in nums:
            # Find the insertion point for num in dp using binary search
            pos = bisect_left(dp, num)

            # If num is greater than all elements in dp, append it to the end
            if pos == len(dp):
                dp.append(num)
            else:
                # Otherwise, replace the element at the found position
                dp[pos] = num

        return len(dp)

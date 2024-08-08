class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            # If k is larger than half the number of days, you can perform as many transactions as needed
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        
        # Initialize DP arrays
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        
        return dp[k][n - 1]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        k = 2  # maximum number of transactions
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for j in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[i][j] = max(dp[i - 1][j], prices[i] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[i])
        
        return dp[-1][k]

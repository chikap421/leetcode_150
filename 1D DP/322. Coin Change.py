class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize a list to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: no coins needed to make amount 0
        
        # Iterate over each amount from 1 to the target amount
        for i in range(1, amount + 1):
            # Check each coin to see if it can be used to form the amount i
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, it means we cannot make the amount with the given coins
        return dp[amount] if dp[amount] != float('inf') else -1

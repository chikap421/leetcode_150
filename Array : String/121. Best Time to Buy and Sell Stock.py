class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit with the current price and update the max profit if needed
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit 
        
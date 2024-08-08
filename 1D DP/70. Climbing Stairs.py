class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # Initialize the base cases
        prev1 = 1  # Number of ways to reach the first step
        prev2 = 2  # Number of ways to reach the second step
        
        # Compute the number of ways to reach each subsequent step
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        
        return prev2

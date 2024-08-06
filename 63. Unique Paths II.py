class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize the DP table
        dp = [[0] * n for _ in range(m)]
        
        # If the starting point is an obstacle, there are no paths
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Start from the top-left corner
        dp[0][0] = 1
        
        # Fill in the first row
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j - 1]
        
        # Fill in the first column
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i - 1][0]
        
        # Fill in the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        
        return dp[-1][-1]

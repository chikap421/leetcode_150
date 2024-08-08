class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= num_rows or c >= num_cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Mark the cell as visited
            # Visit all adjacent cells (up, down, left, right)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':  # Found an island
                    num_islands += 1
                    dfs(r, c)  # Mark all its parts
        
        return num_islands

# Example usage:
solution = Solution()
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))  # Output: 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid2))  # Output: 3

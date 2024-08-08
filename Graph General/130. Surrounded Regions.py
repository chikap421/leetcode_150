class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Temporarily mark this cell
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        # Mark all 'O's connected to the border
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)
        
        # Convert unmarked 'O's to 'X' and 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

# Example usage:
solution = Solution()
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution.solve(board1)
print(board1)  # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

board2 = [["X"]]
solution.solve(board2)
print(board2)  # Output: [["X"]]

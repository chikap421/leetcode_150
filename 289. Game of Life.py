class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        def count_live_neighbors(i, j):
            live_count = 0
            for x in range(max(0, i-1), min(m, i+2)):
                for y in range(max(0, j-1), min(n, j+2)):
                    if (x != i or y != j) and (board[x][y] in (1, -1)):
                        live_count += 1
            return live_count
        
        # Apply the rules
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2
        
        # Update the board to the next state
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

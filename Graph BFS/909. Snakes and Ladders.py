from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        
        def getBoardValue(num):
            # Convert number to board coordinates
            r, c = divmod(num - 1, n)
            if r % 2 == 0:
                # Even row: left to right
                x, y = n - 1 - r, c
            else:
                # Odd row: right to left
                x, y = n - 1 - r, n - 1 - c
            return board[x][y]
        
        # BFS initialization
        queue = deque([(1, 0)])  # (current cell, moves)
        visited = set()
        
        while queue:
            current, moves = queue.popleft()
            
            for i in range(1, 7):
                next_cell = current + i
                if next_cell > n * n:
                    continue
                
                board_value = getBoardValue(next_cell)
                if board_value != -1:
                    next_cell = board_value
                
                if next_cell == n * n:
                    return moves + 1
                
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, moves + 1))
        
        return -1  # If it's not possible to reach the end

# Example usage:
board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,15,-1,-1,-1,-1]]

solution = Solution()
print(solution.snakesAndLadders(board))  # Output: 4

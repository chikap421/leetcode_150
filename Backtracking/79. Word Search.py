class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(x, y, index):
            # If the current index is the length of the word, we have found the word
            if index == len(word):
                return True
            
            # If out of bounds or the current cell does not match the current character in the word
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
                return False
            
            # Mark the cell as visited by changing its value
            temp = board[x][y]
            board[x][y] = '#'
            
            # Explore the adjacent cells in all 4 possible directions
            found = (backtrack(x + 1, y, index + 1) or
                     backtrack(x - 1, y, index + 1) or
                     backtrack(x, y + 1, index + 1) or
                     backtrack(x, y - 1, index + 1))
            
            # Unmark the cell (backtrack)
            board[x][y] = temp
            
            return found
        
        # Iterate over each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start the search from each cell
                if backtrack(i, j, 0):
                    return True
        
        return False

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row, cols, diags, anti_diags):
            if row == n:
                return 1
            
            solutions = 0
            for col in range(n):
                diag = row - col
                anti_diag = row + col
                if col in cols or diag in diags or anti_diag in anti_diags:
                    continue
                
                # Place the queen
                cols.add(col)
                diags.add(diag)
                anti_diags.add(anti_diag)
                
                # Move to the next row
                solutions += backtrack(row + 1, cols, diags, anti_diags)
                
                # Remove the queen
                cols.remove(col)
                diags.remove(diag)
                anti_diags.remove(anti_diag)
            
            return solutions
        
        return backtrack(0, set(), set(), set())

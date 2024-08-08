class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        # Create an array of strings for all rows
        rows = [''] * min(numRows, len(s))
        
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to get the final string
        return ''.join(rows)

# Example usage
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))  # Output: "A"

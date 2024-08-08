class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Resultant list to store the combinations
        result = []
        
        # Backtracking function
        def backtrack(index, path):
            # If the path length equals the length of digits, we have a complete combination
            if index == len(digits):
                result.append("".join(path))
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                # Add the letter to the current path
                path.append(letter)
                # Move to the next digit
                backtrack(index + 1, path)
                # Backtrack, remove the letter from the path
                path.pop()
        
        # Initialize the backtracking process
        backtrack(0, [])
        return result

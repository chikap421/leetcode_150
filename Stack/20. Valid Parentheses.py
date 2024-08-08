class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a stack to keep track of opening brackets
        stack = []
        # Create a mapping of closing to opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty
                # Otherwise assign a dummy value of '#' to top_element
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket doesn't match the stack's top element
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all the opening brackets have been matched
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("{[]}"))  # Output: True

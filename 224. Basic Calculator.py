class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                result *= stack.pop()  # sign before the parenthesis
                result += stack.pop()  # result calculated before the parenthesis

        result += sign * current_number
        return result

# Example usage:
solution = Solution()
print(solution.calculate("1 + 1"))  # Output: 2
print(solution.calculate(" 2-1 + 2 "))  # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23

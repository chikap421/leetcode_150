class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # To ensure the division truncates towards zero
                    if a * b < 0 and a % b != 0:
                        stack.append(a // b + 1)
                    else:
                        stack.append(a // b)
            else:
                stack.append(int(token))
        
        return stack[0]

# Example usage:
solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"]))  # Output: 9
print(solution.evalRPN(["4","13","5","/","+"]))  # Output: 6
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22

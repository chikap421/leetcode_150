class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                total_sum += digit ** 2
            return total_sum
        
        seen_numbers = set()
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next(n)
        
        return n == 1

# Example usage:
# solution = Solution()
# print(solution.isHappy(19))  # Output: true
# print(solution.isHappy(2))   # Output: false

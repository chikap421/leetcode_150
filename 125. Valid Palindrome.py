class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Normalize the string
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Use two-pointer technique to check for palindrome
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(solution.isPalindrome("race a car"))  # Output: false
print(solution.isPalindrome(" "))  # Output: true

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Check for even-length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest

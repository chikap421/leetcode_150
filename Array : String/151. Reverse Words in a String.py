class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Trim the string to remove leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words
        words = s.split()
        
        # Step 3: Reverse the list of words
        words.reverse()
        
        # Step 4: Join the reversed words into a single string
        reversed_s = ' '.join(words)
        
        return reversed_s

# Example usage
solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
print(solution.reverseWords("a good   example"))  # Output: "example good a"

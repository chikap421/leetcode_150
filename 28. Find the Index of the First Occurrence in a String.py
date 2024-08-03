class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: If needle is an empty string
        if not needle:
            return 0
        
        # Lengths of haystack and needle
        len_h = len(haystack)
        len_n = len(needle)
        
        # If needle is longer than haystack, it cannot be a substring
        if len_n > len_h:
            return -1
        
        # Sliding window approach
        for i in range(len_h - len_n + 1):
            # Check if the substring of haystack from i to i + len_n matches needle
            if haystack[i:i + len_n] == needle:
                return i
        
        # If no match found
        return -1

# Example usage
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 0
print(solution.strStr("leetcode", "leeto"))  # Output: -1

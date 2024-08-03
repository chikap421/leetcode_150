class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t

# Example usage:
# s = "anagram"
# t = "nagaram"
# solution = Solution()
# print(solution.isAnagram(s, t))  # Output: True

# s = "rat"
# t = "car"
# print(solution.isAnagram(s, t))  # Output: False

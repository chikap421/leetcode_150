from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        # Dictionary to count all characters in t
        t_count = Counter(t)
        # Dictionary to count characters in the current window of s
        window_count = defaultdict(int)
        
        # Number of unique characters in t that need to be present in the window
        required = len(t_count)
        # Number of unique characters in the current window that match the required count in t
        formed = 0
        
        left = 0
        right = 0
        
        min_length = float("inf")
        min_window = (0, 0)
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_length == float("inf") else s[min_window[0]:min_window[1] + 1]

# Example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))                # Output: "a"
print(solution.minWindow("a", "aa"))               # Output: ""

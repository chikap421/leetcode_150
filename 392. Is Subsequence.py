class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# Example usage
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: true
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: false

# Follow-Up Optimization
# Here's an optimized approach for multiple 's' strings:
# import bisect

# class Solution:
#     def __init__(self):
#         self.t_index_map = {}

#     def preprocess(self, t):
#         from collections import defaultdict
#         self.t_index_map = defaultdict(list)
#         for index, char in enumerate(t):
#             self.t_index_map[char].append(index)
    
#     def isSubsequence(self, s, t):
#         # Use two-pointer approach for a single check
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)

#     def isSubsequenceOptimized(self, s):
#         prev_index = -1
#         for char in s:
#             if char not in self.t_index_map:
#                 return False
#             # Get the index of the smallest number in the list which is > prev_index
#             idx_list = self.t_index_map[char]
#             idx = bisect.bisect_right(idx_list, prev_index)
#             if idx == len(idx_list):
#                 return False
#             prev_index = idx_list[idx]
#         return True

# # Example usage
# solution = Solution()
# solution.preprocess("ahbgdc")  # Preprocess the fixed string t
# print(solution.isSubsequenceOptimized("abc"))  # Output: true
# print(solution.isSubsequenceOptimized("axc"))  # Output: false

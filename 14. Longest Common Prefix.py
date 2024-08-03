class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Step 1: Handle edge case where input list is empty
        if not strs:
            return ""
        
        # Step 2: Find the shortest string in the list
        shortest_str = min(strs, key=len)
        
        # Step 3: Compare characters
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        
        return shortest_str

# Example usage
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for string in strs:
            # Sort the string to use as a key
            sorted_string = ''.join(sorted(string))
            
            # Add the original string to the list of anagrams for this key
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
        
        # Return the list of all groups of anagrams
        return list(anagrams.values())

# Example usage:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# solution = Solution()
# print(solution.groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length found
                max_length = max(max_length, current_length)
        
        return max_length

# Example usage:
# solution = Solution()
# print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
# print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9

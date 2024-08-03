class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the complement and its index
        num_to_index = {}
        
        # Iterate over the list
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # If the complement is in the dictionary, return the pair of indices
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the index of the current number
            num_to_index[num] = index

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# print(solution.twoSum(nums, target))  # Output: [0, 1]

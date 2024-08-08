class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Resultant list to store all permutations
        result = []
        
        # Backtracking function
        def backtrack(start):
            # If we have a complete permutation
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Iterate over the indices
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next element
                backtrack(start + 1)
                # Backtrack, undo the swap
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start the backtracking with the first element
        backtrack(0)
        return result

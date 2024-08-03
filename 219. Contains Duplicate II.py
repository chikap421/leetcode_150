class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}  # Hashmap to store the index of each element
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update the latest index of the current element
        
        return False

# Example usage:
# solution = Solution()
# print(solution.containsNearbyDuplicate([1,2,3,1], 3))  # Output: true
# print(solution.containsNearbyDuplicate([1,0,1,1], 1))  # Output: true
# print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # Output: false

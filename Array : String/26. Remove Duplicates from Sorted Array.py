class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        # Initialize the slow pointer
        slow = 1

        # Iterate with the fast pointer from the second element
        for fast in range(1, len(nums)):
            # Check if the current element is different from the previous one 
            if nums[fast] != nums[fast -1]:
                # Assign the unique element to the slow pointer position
                nums[slow] = nums[fast]
                # Move the slow pointer to the next position
                slow += 1
        # The slow pointer indicates the number of unique elements      
        return slow
        
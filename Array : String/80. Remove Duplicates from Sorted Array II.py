class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        # Initialize the slow pointer
        slow = 2

        # Iterate with the fast pointer starting from the third element
        for fast in range(2, len(nums)):
            # Check if the current element is different from the element at slow-2
            if nums[fast] != nums[slow -2]:
                # Assign the unique element to the slow pointer position
                nums[slow] = nums[fast]
                # Move the slow pointer to the next position
                slow +=1
        
        # The slow pointer indicates the number of unique elements which are allowed twice
        return slow

        

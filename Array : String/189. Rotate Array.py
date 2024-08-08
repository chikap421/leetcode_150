class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # In case k is greater than n
        k %= n 

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(0, n - 1)

        # Reverse the first k elements
        reverse(0, k - 1)

        # Reverse the remaining n - k elements
        reverse(k, n - 1)
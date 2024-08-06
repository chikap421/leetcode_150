class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            # Compare middle element with its next element
            if nums[mid] > nums[mid + 1]:
                return binary_search(left, mid)
            else:
                return binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)

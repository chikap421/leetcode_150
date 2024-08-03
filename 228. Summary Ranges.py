class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums:
            return result

        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = end = nums[i]

        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))

        return result

# Example usage:
solution = Solution()
print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))  # Output: ["0->2", "4->5", "7"]
print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # Output: ["0", "2->4", "6", "8->9"]

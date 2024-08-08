class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort balloons by their end positions
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for interval in points[1:]:
            if interval[0] > end:
                arrows += 1
                end = interval[1]
        
        return arrows

# Example usage:
solution = Solution()
print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # Output: 2
print(solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))  # Output: 4
print(solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))  # Output: 2

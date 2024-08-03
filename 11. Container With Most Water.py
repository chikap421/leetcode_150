class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with the current left and right pointers
            width = right - left
            current_area = min(height[left], height[right]) * width
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage
solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(solution.maxArea([1, 1]))                       # Output: 1

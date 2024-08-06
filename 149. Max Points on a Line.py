from collections import defaultdict

# Custom gcd function for compatibility with older Python versions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def get_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return ('inf', p1[0])
            g = gcd(dx, dy)
            return (dy // g, dx // g)
        
        if len(points) <= 1:
            return len(points)
        
        max_points = 1
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            same_point_count = 1
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same_point_count += 1
                else:
                    slope = get_slope(points[i], points[j])
                    slopes[slope] += 1
            
            max_slope_points = max(slopes.values()) if slopes else 0
            max_points = max(max_points, same_point_count + max_slope_points)
        
        return max_points

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build the graph
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # Visited states: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:  # Found a cycle
                return False
            if visited[course] == 2:  # Already processed
                return True
            
            # Mark the course as being visited
            visited[course] = 1
            
            # Visit all the adjacent nodes
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # Mark the course as fully processed
            visited[course] = 2
            return True
        
        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

# Example usage:
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))  # Output: False

numCourses = 2
prerequisites = [[1, 0]]
print(solution.canFinish(numCourses, prerequisites))  # Output: True

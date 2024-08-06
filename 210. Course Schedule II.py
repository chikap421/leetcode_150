from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Initialize graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            # Reduce in-degree of neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all courses are in the order, return the order
        if len(order) == numCourses:
            return order
        else:
            return []

# Example usage:
numCourses = 2
prerequisites = [[1, 0]]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))  # Output: [0, 1]

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(solution.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]

numCourses = 1
prerequisites = []
print(solution.findOrder(numCourses, prerequisites))  # Output: [0]

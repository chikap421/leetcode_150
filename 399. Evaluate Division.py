from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        
        # Build the graph
        for (start, end), value in zip(equations, values):
            graph[start][end] = value
            graph[end][start] = 1 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()
            
            while queue:
                current, current_value = queue.popleft()
                if current == end:
                    return current_value
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, current_value * value))
            
            return -1.0
        
        results = []
        for start, end in queries:
            results.append(bfs(start, end))
        
        return results

# Example usage:
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
solution = Solution()
print(solution.calcEquation(equations, values, queries))

import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        # Step 1: Combine the projects' capital and profit into a list of tuples
        projects = list(zip(capital, profits))
        # Step 2: Sort the projects by their capital requirement
        projects.sort()
        
        # Initialize the max heap for profits
        max_heap = []
        idx = 0
        n = len(projects)
        
        # Step 3: Perform k iterations to select projects
        for _ in range(k):
            # Push all feasible projects into the max heap
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])  # We use negative profit because heapq is a min-heap by default
                idx += 1
            # If the heap is empty, no more projects can be selected
            if not max_heap:
                break
            # Select the project with the maximum profit
            w -= heapq.heappop(max_heap)  # Pop the max profit from the heap (remember, it is stored as negative)
        
        return w

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Resultant list to store all combinations
        result = []
        
        # Backtracking function
        def backtrack(start, path):
            # If the combination is complete
            if len(path) == k:
                result.append(path[:])
                return
            
            # Iterate from the current number to n
            for i in range(start, n + 1):
                # Add the number to the current path
                path.append(i)
                # Recurse with the next number as start
                backtrack(i + 1, path)
                # Backtrack, remove the last number
                path.pop()
        
        # Start the backtracking with the first number
        backtrack(1, [])
        return result

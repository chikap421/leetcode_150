class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path, remaining):
            # Base case: if remaining sum is zero, we found a combination
            if remaining == 0:
                result.append(path[:])
                return
            # Iterate over the candidates starting from 'start'
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                # If the candidate exceeds the remaining sum, skip
                if candidate > remaining:
                    continue
                # Include the candidate in the current path and recurse
                path.append(candidate)
                backtrack(i, path, remaining - candidate)
                # Backtrack: remove the last candidate from the path
                path.pop()
        
        # Start backtracking from index 0 with an empty path and the target sum
        backtrack(0, [], target)
        return result

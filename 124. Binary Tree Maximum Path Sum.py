# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the max path sum of left and right subtrees
            left_max = max(dfs(node.left), 0)  # Only consider positive sums
            right_max = max(dfs(node.right), 0)  # Only consider positive sums
            
            # Current path sum including the current node
            current_path_sum = node.val + left_max + right_max
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum sum path of the current node being part of the higher path
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.max_sum

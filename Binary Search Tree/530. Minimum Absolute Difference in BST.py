# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')
        self.in_order_traversal(root)
        return self.min_diff
    
    def in_order_traversal(self, node):
        if node is None:
            return
        
        # In-order traversal: left -> node -> right
        self.in_order_traversal(node.left)
        
        # Process the current node
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val
        
        self.in_order_traversal(node.right)

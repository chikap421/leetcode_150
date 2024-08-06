# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = None
        self.in_order_traversal(root)
        return self.result
    
    def in_order_traversal(self, node):
        if node is None:
            return
        
        # Traverse the left subtree
        self.in_order_traversal(node.left)
        
        # Process the current node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        
        # Traverse the right subtree
        self.in_order_traversal(node.right)

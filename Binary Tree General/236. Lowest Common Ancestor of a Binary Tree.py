# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If the root is None, we return None
        if not root:
            return None
        
        # If we find either p or q, we return the root
        if root == p or root == q:
            return root
        
        # Recursively search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null value between left and right
        return left if left else right

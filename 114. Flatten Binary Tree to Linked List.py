# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Helper function to flatten the tree
        def flatten_tree(node):
            if not node:
                return None
            
            # Flatten the left and right subtrees
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)
            
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            # We need to return the "tail" of the flattened subtree
            return right_tail if right_tail else left_tail if left_tail else node
        
        flatten_tree(root)

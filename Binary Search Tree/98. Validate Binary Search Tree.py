# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self, node, low, high):
        # An empty tree is a valid BST
        if node is None:
            return True
        
        # The current node's value must be between low and high
        if not (low < node.val < high):
            return False
        
        # Recursively check the left subtree and right subtree
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)

# Example usage:
# Constructing the example tree:
#      2
#     / \
#    1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
print(solution.isValidBST(root))  # Output should be True

# Example where the tree is not a valid BST:
#      5
#     / \
#    1   4
#       / \
#      3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(solution.isValidBST(root))  # Output should be False

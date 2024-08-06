# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Calculate the height of the tree
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        height = compute_height(root)
        if height == 0:
            return 0
        
        # Binary search to count nodes at the last level
        def exists(index, height, node):
            left, right = 0, 2**(height-1) - 1
            for _ in range(height - 1):
                mid = (left + right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None
        
        left, right = 0, 2**(height-1) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1
        
        # Total nodes = full tree nodes + nodes in the last level
        return (2**(height-1) - 1) + left

# Example usage:
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# solution = Solution()
# print(solution.countNodes(root))  # Output: 3

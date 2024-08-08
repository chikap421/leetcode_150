# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.pop(0)
                if left_to_right:
                    level_values.append(node.val)
                else:
                    level_values.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)
            left_to_right = not left_to_right

        return result

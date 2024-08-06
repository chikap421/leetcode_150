# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        """
        Helper function to add all the nodes along the leftmost path
        starting from the root.
        """
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # If the node has a right child, add all the leftmost nodes of the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        
        return topmost_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

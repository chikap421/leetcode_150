# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        # Start with the root node
        current = root
        
        # We will use dummy to keep track of the start of the next level
        dummy = Node(0)
        
        while current:
            # Use an iterator for the current level
            iter_node = dummy
            dummy.next = None
            
            # Traverse the current level
            while current:
                if current.left:
                    iter_node.next = current.left
                    iter_node = iter_node.next
                if current.right:
                    iter_node.next = current.right
                    iter_node = iter_node.next
                current = current.next
            
            # Move to the next level
            current = dummy.next
        
        return root

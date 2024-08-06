# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def convertListToBST(left, right):
            if left > right:
                return None
            
            # always choose left middle node as a root
            mid = (left + right) // 2
            
            # root element
            node = TreeNode(nums[mid])
            
            # recursively build the left subtree
            node.left = convertListToBST(left, mid - 1)
            
            # recursively build the right subtree
            node.right = convertListToBST(mid + 1, right)
            
            return node
        
        return convertListToBST(0, len(nums) - 1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''Can also use inorder traversal get the odered list if validate BST'''
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, sys.maxint, -sys.maxint)
    def helper(self, root, minVal, maxVal):
        if not root: return True
        if root.val >= maxVal or root.val <= minVal: return False
        return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        queue = [root]
        while queue:
            result.append([item.val for item in queue])
            tempQueue = []
            for item in queue:
                if item.left: tempQueue.append(item.left)
                if item.right: tempQueue.append(item.right)
            queue = tempQueue
        return result[::-1]
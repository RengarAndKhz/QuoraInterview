# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        queue = [(0,root)]
        while queue:
            tempNum, temp = queue.pop(0)
            if len(result) <= tempNum:
                result.append([temp.val])
            else:
                result[tempNum] += [temp.val]
            if temp.left:
                queue.append((tempNum+1,temp.left))
            if temp.right:
                queue.append((tempNum+1,temp.right))
        return result

    def version2(self, root):
        if not root: return []
        result = []
        queue = [root]
        while queue:
            result.append([temp.val for temp in queue])
            newQueue = []
            for item in queue:
                if item.left:
                    newQueue.append(item.left)
                if item.right:
                    newQueue.append(item.right)
            queue = newQueue
        return result
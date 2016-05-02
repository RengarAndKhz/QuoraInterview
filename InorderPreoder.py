# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#O(n^2) every node in postorder need index of in inorder
class Solution(object):
    '''def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return None
        temp = postorder.pop()

        root = TreeNode(temp)
        index = inorder.index(temp)
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root'''
    def buildTree(self, inorder, postorder):
        dictionary = {val:i for i, val in enumerate(inorder)}
        return self.helper(0, len(inorder), inorder, postorder, dictionary)

    def helper(self, lin, rin, inorder, postorder, dictionary):
        if lin < rin:
            root = TreeNode(postorder.pop())
            index = dictionary[root.val]
            root.right = self.helper(index+1, rin, inorder, postorder, dictionary)
            root.left = self.helper(lin, index, inorder, postorder, dictionary)
            return root


list = [1,2,3]
print(list.index(3))

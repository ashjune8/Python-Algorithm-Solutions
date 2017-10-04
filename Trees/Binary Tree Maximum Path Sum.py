# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """


    def findsum(root):

        if root.left == None and root.right == None:
            return root.val
        elif root.right == None:
            return findsum(root.left)
        elif root.left == None:
            return findsum(root.right)
        else:


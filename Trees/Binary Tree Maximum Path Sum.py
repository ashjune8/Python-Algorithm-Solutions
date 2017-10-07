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
            return root.val + findsum(root.left)
        elif root.left == None:
            return root.val + findsum(root.right)
        else:
            return root.val + findsum(root.left) + findsum(root.right)

    return findsum(root)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

print maxPathSum(a)
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    if root.left != None and root.left.left == None and root.left.right == None:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)



a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

a.right.left = TreeNode(7)
a.right.right = TreeNode(6)

print sumOfLeftLeaves(a)


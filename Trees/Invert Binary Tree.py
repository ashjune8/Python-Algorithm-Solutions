# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """


    if root == None:
        return None
    else:
        temp = TreeNode(root.val)
        x = temp.val
        temp.left = invertTree(root.right)
        temp.right = invertTree(root.left)
        return temp

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
print invertTree(a).right.right.val
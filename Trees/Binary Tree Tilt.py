# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def findTilt(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if root == None:
        return 0
    def nodesum(root):
        if root == None:
            return 0
        else:
            return root.val+ nodesum(root.left) + nodesum(root.right)

    return abs(nodesum(root.left) - nodesum(root.right)) + findTilt(root.left) + findTilt(root.right)

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.right.left = TreeNode(5)

print findTilt(a)
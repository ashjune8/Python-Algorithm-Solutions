# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1;


    def findmin(root):
        if(root.left == None and root.right) == None:
            return 1
        elif root.left == None:
            return 1 + findmin(root.right)
        elif root.right == None:
            return 1 + findmin(root.left)
        else:
            return min((1+findmin(root.left)),(1+findmin(root.right)))

    return findmin(root)
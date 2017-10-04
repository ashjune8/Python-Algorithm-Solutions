# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None:
        return True
    lefttree = root.left
    righttree = root.right



    def mirrorcheck(lefttree,righttree):

        if lefttree == None and righttree == None:
            return True
        elif lefttree == None or righttree == None:
            return False

        #x = lefttree.val
        #y = righttree.val
        elif lefttree.val != righttree.val:
            return False

        else:
            return mirrorcheck(lefttree.left, righttree.right) == True and mirrorcheck(lefttree.right,
                                                                                       righttree.left) == True

    return mirrorcheck(lefttree,righttree)

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(2)
a.left.left = TreeNode(5)
a.left.right = TreeNode(4)
a.right.left = TreeNode(4)
a.right.right = TreeNode(5)

print isSymmetric(a)


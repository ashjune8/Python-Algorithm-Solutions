class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def printleafnode(root):

    if root.left == None and root.right == None:
        print root.val
    elif root.left == None:
        printleafnode(root.right)
    elif root.right == None:
        printleafnode(root.left)
    else:
        printleafnode(root.right)
        printleafnode(root.left)


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)

printleafnode(a)
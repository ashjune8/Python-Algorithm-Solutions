# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    if p == None and q == None:
        return True

    if (p == None and q != None) or (p != None and q == None):
        return False
    x = p.val
    y = q.val

    if p.val != q.val:
        return False
    else:
        return (isSameTree(p.left,q.left) == True) and (isSameTree(p.right,q.right) == True)



a = TreeNode(10)
a.left = TreeNode(5)
a.right = TreeNode(15)
b = TreeNode(10)
b.left = TreeNode(5)
b.right = None
b.left.left = None
b.left.right = TreeNode(15)

print isSameTree(a,b)

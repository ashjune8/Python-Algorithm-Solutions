# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def tree2str(t):
    """
    :type t: TreeNode
    :rtype: str
    """
    if t == None:
        return ''
    if t.left == None and t.right == None:
        return str(t.val)
    if t.right == None:
        return str(t.val) + '(' + tree2str(t.left) + ')'


    else:
        return str(t.val) + '(' + tree2str(t.left) +')' + '(' + tree2str(t.right) + ')'

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)
print tree2str(a)
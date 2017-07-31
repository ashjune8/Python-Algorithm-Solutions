# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



def getMinimumDifference(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if root.left == None and root.right == None:
        return root.val
    if root.left == None:
        right = abs(root.val - root.right.val)
        return min(right,getMinimumDifference(root.right))
    if root.right == None:
        left = abs(root.val - root.left.val)
        return min(left,getMinimumDifference(root.left))
    else:
        left = abs(root.val - root.left.val)
        right = abs(root.val - root.right.val)
        return min(left,right,getMinimumDifference(root.left),getMinimumDifference(root.right))

tree1 = TreeNode(0)
tree1.left = TreeNode(2)
tree1.right = TreeNode(5)
tree1.left.left = TreeNode(4)
print getMinimumDifference(tree1)


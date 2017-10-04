# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    checklist = []
    if t1 == None and t2 == None:
        return None
    elif t1 == None:
        return t2
    elif t2 == None:
        return t1

    else:
        temp = TreeNode(t1.val + t2.val)
        checklist.append(temp.val)
        temp.left = mergeTrees(t1.left,t2.left)
        temp.right = mergeTrees(t1.right,t2.right)
        return temp

tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(4)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)

print mergeTrees(tree1,tree2).left.left.val
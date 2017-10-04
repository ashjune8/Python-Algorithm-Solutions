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
    list = []

    def addlist(node,list):
        if node.left != None:
            addlist(node.left,list)
        list.append(node.val)
        if node.right != None:
            addlist(node.right,list)
        return list

    list = addlist(root,list)

    return min([abs(a - b) for a, b in zip(list, list[1:])])




    return minimum

tree1 = TreeNode(0)
tree1.left = TreeNode(2)
tree1.right = TreeNode(5)
tree1.left.left = TreeNode(4)
print getMinimumDifference(tree1)

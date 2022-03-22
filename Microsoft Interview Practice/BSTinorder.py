class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def inOrdertreeTraversal(root):

        if root.left != None:
            inOrdertreeTraversal(root.left)

        finalList.append(root.val)

        if root.right != None:
            inOrdertreeTraversal(root.right)
            
    if root == None:
        return root
    finalList = []
    inOrdertreeTraversal(root)
    return finalList
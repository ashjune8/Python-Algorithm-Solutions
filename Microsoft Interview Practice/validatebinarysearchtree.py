# https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/152/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    def inOrdertreeTraversal(root):

        if root.left != None:
            inOrdertreeTraversal(root.left)

        finalList.append(root.val)

        if root.right != None:
            inOrdertreeTraversal(root.right)
            
    
    if root == None:
        return True
    elif root.left == None and root.right == None:
        return True
    else:

        finalList = []
        inOrdertreeTraversal(root)
        if len(set(finalList)) != len(finalList):
            return False
        elif finalList == sorted(finalList):
            return True
        else:
            return False
        
        

        



    

a = TreeNode(1)
b = TreeNode(5)
c = TreeNode(4)
d = TreeNode(3)
e = TreeNode(6)
b.left = a
b.right = c
c.left = d
c.right = e


print (isValidBST(b))
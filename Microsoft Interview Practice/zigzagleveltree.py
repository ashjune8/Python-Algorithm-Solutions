# https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/197/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    level = 1
    kvp = {}

    if root == None:
        return None
    
    
    def postTraversal(root, level, kvp):

        if  level not in kvp:
            kvp[level] = []
        
        kvp[level].append(root.val)

        if root.left != None:
            postTraversal(root.left,level+ 1, kvp)

        if root.right != None:
            postTraversal(root.right, level + 1, kvp)

    postTraversal(root,level,kvp)

    i = 1
    finalList = []

    while i in kvp:
        finalList.append(kvp[i])
        i += 1

    zigZagFlag = False

    for i in range(len(finalList)):
        if zigZagFlag:
            finalList[i] = finalList[i][::-1]
            zigZagFlag = False
        else:
            zigZagFlag = True

    return finalList

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
c.right = d

print (zigzagLevelOrder(a))

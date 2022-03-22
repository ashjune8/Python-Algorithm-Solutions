# https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/192/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



def connect(root):
    """
    :type root: Node
    :rtype: Node
    """

    level = 1
    kvp = {}

    if root == None:
        return None
    
    
    def postTraversal(root, level, kvp):

        if  level not in kvp:
            kvp[level] = []
        
        kvp[level].append(root)

        if root.left != None:
            postTraversal(root.left,level+ 1, kvp)

        if root.right != None:
            postTraversal(root.right, level + 1, kvp)

    postTraversal(root,level,kvp)

    i = 1
    

    while i in kvp:
        j = 0
        for j in range(len(kvp[i])-1):
            kvp[i][j].next = kvp[i][j+1]
            
        j = 0
        i += 1

    return kvp[1][0]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
c.right = d

print (connect(a).val)

# https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/163/

class Node(object):
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

        finalList = {}
        level = 1
        tempList = []

        if root == None:
            return root

        def traversal(root, level):

            if finalList.get(level) == None:
                finalList[level]=[]
                finalList[level].append(root)
            else:
                finalList[level].append(root)

            if root.left != None:
                traversal(root.left, level + 1)

            if root.right != None:
                traversal(root.right, level + 1)

        traversal(root,level)

        i = 1

        while i in finalList:
            for j in range(len(finalList[i])-1):
                finalList[i][j].next = finalList[i][j+1]
            i += 1
        
        return finalList[1][0]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.left = b
a.right = c
c.right = d

print (connect(a))

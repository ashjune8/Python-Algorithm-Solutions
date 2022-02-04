# https://practice.geeksforgeeks.org/problems/mirror-tree/1/?company[]=Amazon&company[]=Amazon&page=1&query=company[]Amazonpage1company[]Amazon

class Node(object):
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def mirror(root):
    if(root == None):
        return
    elif(root.left == None and root.right == None):
        return
    elif(root.left != None and root.right != None):
        temp = root.right
        root.right = root.left
        root.left = temp
        mirror(root.left)
        mirror(root.right)
    elif(root.left != None):
        root.right = root.left
        root.left = None
        mirror(root.left)
        mirror(root.right)
    elif(root.right != None):
        root.left = root.right
        root.right = None
        mirror(root.left)
        mirror(root.right)
    else:
        return






a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.right = c
a.left = b


mirror(a)
print a.right.data
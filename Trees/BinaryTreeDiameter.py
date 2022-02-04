# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    elif root.left and root.right:
        return 1 +  max(height(root.left),height(root.right))
    elif root.left != None:
        return 1 + height(root.left)
    else:
        return 1 + height(root.right) 


def diameter(root):
    if root == None:
        return 0
    else: 
        return max(1 + height(root.left) + height(root.right), diameter(root.left), diameter(root.right))


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
c.right = d
d.left = e

print (diameter(a))

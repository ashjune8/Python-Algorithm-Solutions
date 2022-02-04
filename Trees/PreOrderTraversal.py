class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)



def preOrder(root):
    #Write your code here

    

    

    if root == None:
        return root

    print (root.info),

    if(root.left != None):
        preOrder(root.left)

    if(root.right != None):
        preOrder(root.right)

a = Node(1)
b = Node(2)
c = Node (3)
d = Node (4)

a.left = b
a.right = c
c.left = d

preOrder(a)




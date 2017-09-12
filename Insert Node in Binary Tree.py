class Node:
    def __init__(self, info):
        self.data = info
        self.left = None
        self.right = None

def insert(r,val):
    temp = Node(val)




    def insertinrightposition(r,temp):

        x =  r.data

        if r.right == None and r.left == None and temp.data < r.data:
            r.left = temp
        elif r.right == None and r.left == None and temp.data > r.data:
            r.right = temp
        elif temp.data < r.data and r.left != None:
            insertinrightposition(r.left,temp)

        elif temp.data > r.data and r.right != None:
            insertinrightposition(r.right,temp)
    if r == None:
        return temp
    insertinrightposition(r,temp)
    return r

a = Node(4)
b = Node(2)
c = Node(7)
d = Node(1)
e = Node(3)
a.left = b
a.right = c
b.left = d
b.right = e
print insert(a,6).right.left.data


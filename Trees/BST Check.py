class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    lst = []

    def inOrder(root):

        if root.left != None:
            inOrder(root.left)

        lst.append(root.data)

        if root.right != None:
            inOrder(root.right)
    inOrder(root)
   # print lst
    if len(lst) != len(set(lst)):
        return False
    if lst == sorted(lst):
        return True
    else:
        return False

lst = []
def inorder_new(root):
    if root != None:
        inorder_new(root.left)
        lst.append(root.data)
        inorder_new(root.right)

    return lst



a = node(2)
b = node(1)
c = node(3)
d = node(4)
a.left = b
a.right = c
c.right = d
print checkBST(a)
print inorder_new(a)

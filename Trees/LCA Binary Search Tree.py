class Node:
    def __init__(self, info):
        self.data = info
        self.left = None
        self.right = None

def lca(root , v1 , v2):

    if v2 < v1:
        temp = v1
        v1 = v2
        v2 = temp



    def findlca(root,v1,v2):

        x = root.data

        if v1 < root.data and v2 < root.data:
            return findlca(root.left, v1, v2)
        if v1 > root.data and v2 > root.data:
            return findlca(root.right, v1, v2)
        else:
            return root

    return findlca(root,v1,v2).data









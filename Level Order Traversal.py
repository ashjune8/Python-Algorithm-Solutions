class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def levelOrder(root):
   #Write code Here

    lst = []
    lst.insert(0,root)

    while lst != []:
        if lst[len(lst)-1] == None:
            lst.pop()
        else:
            print lst[len(lst)-1].info,
            lst.insert(0,lst[len(lst)-1].left)
            lst.insert(0, lst[len(lst) - 1].right)
            lst.pop()
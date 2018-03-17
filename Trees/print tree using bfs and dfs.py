class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root):
    queue = []
    queue.append(root)
    lst = []
    lst.append(root.val)

    while queue != []:
        temp = queue.pop()
        if temp.left != None:
            queue.append(temp.left)
            lst.append(temp.left.val)
        if temp.right != None:
            queue.append(temp.right)
            lst.append(temp.right.val)
    return lst

dfslst = []
# preorder
def dfs(root,dfslst):

    if root != None:
        dfslst.append(root.val)
        dfs(root.left,dfslst)
        dfs(root.right,dfslst)

    return dfslst




a = TreeNode(10)
a.left = TreeNode(5)
a.right = TreeNode(15)

a.left.left = TreeNode(10)


print dfs(a,dfslst)

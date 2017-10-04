# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    listoflist =[]
    lst = []
    queue = []
    queue.insert(0,root)
    temp = 0


    while queue != []:
        temp = len(queue)
        for i in range(temp):
            if queue[i] == None:
                continue
            lst.insert(0,queue[i].val)
        listoflist.append(lst)
        lst = []
        for i in range(temp):
            if queue[len(queue)-1] == None:
                queue.pop(len(queue)-1)
                continue
            else:
                queue.insert(0,queue[len(queue)-1].left)
                queue.insert(0,queue[len(queue)-1].right)
                queue.pop(len(queue)-1)
    return listoflist[::-1][1:]


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(5)
a.left.right = TreeNode(4)


print levelOrderBottom(a)

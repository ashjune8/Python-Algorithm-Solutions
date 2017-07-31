#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = []
    level = 0
    queue.insert(0,root)

    while queue != []:
        temp = len(queue)
        for i in range(temp):
            if queue[len(queue)-1] == None:
                queue.pop()
                continue
            else:
                queue.insert(0,queue[len(queue)-1].left)
                queue.insert(0,queue[len(queue)-1].right)
                queue.pop()
        level += 1

    return level - 1

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(5)
a.left.right = TreeNode(4)

print maxDepth(a)


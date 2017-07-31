# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    result = []
    queue = []

    temp = 0.0
    sum = 0.0
    nonecount = 0.0
    queue.insert(0,root)

    while queue != []:
        temp = len(queue)
        for i in range(temp):
            if queue[len(queue)-1] == None:
                queue.pop()
                nonecount += 1.0
                continue
            else:
                queue.insert(0,queue[len(queue)-1].left)
                queue.insert(0,queue[len(queue)-1].right)
                sum += queue.pop().val
        if temp == nonecount:
            break
        result.append(float(sum/(temp-nonecount)))
        sum = 0.0
        nonecount = 0.0

    return result

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(5)

print averageOfLevels(a)


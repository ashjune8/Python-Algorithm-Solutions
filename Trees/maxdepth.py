# https://www.interviewbit.com/problems/max-depth-of-binary-tree/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(A):
    
    if (A.left != None and A.right != None):
        return max(1 + maxDepth(A.left), 1 + maxDepth(A.right))
    if (A.left != None):
        return (1 + maxDepth(A.left))
    if (A.right != None):
        return (1 + maxDepth(A.right))
    else:
        return 1

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
b.left = c
c.right = d

print maxDepth(a)
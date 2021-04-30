# https://www.interviewbit.com/problems/next-pointer-binary-tree/

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):

    traverse(root)
    return root

    


def traverse(root):
        if(root.right != None):
            root.next = None
            traverse(root.right)
        else:
            root.next = None
            
    
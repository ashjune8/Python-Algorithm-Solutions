# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1/?company[]=Amazon&company[]=Amazon&page=1&query=company[]Amazonpage1company[]Amazon

class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None

def height(root):

    if(root.left and root.right):
        return max(1 + height(root.left), 1+ height(root.right))
    if(root.left != None):
        return 1 + height(root.left)
    if(root.right != None):
        return 1 + height(root.right)
    if(root.left == None or root.right == None):
        return 1

a=Node(2)
b=Node(1)
c=Node(3)
a.right = b
b.left = c

print height(a)
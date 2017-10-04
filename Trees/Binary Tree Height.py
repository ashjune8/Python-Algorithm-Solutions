
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None




def height(root):


    if root.left == None and root.right == None:
        return 0
    elif root.left == None:
        return 1 + height(root.right)
    elif root.right == None:
        return 1 + height(root.left)
    else:
        return 1 + max(height(root.right),height(root.left))




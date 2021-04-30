# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None

def lca(root, v1, v2):

    if(root.info < v1 and root.info < v2):
        lca(root.right,v1,v2)
    if(root.info > v1 and root.info > v2):
        lca(root.left,v1,v2)
    else:
        return root

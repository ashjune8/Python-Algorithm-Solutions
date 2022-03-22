


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root,p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return root
        
        def traversal(root):

            if p.val<root.val and q.val<root.val:
                return traversal(root.left)
            elif p.val>root.val and q.val>root.val:
                return traversal(root.right)
            else:
                return root
        return traversal(root)

a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)

a.left = b
a.right = c
b.left = TreeNode(0)
b.right = TreeNode(4)
b.right.left = TreeNode(3)
b.right.right = TreeNode(5)
c.left = TreeNode(7)
c.right = TreeNode(9)

print (lowestCommonAncestor(a,2,8).val)

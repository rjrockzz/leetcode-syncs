# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
Please note that p and q always exist in the tree.
* Since we dfs from the root down to its children, if current root == p or root == q then current root must be   their LCA.
* If left subtree contains one of descendant (p or q) and right subtree contains the remaining descendant (q     or p) then the root is their LCA.
* If left subtree contains both p and q then return left as their LCA.
* If right subtree contains both p and q then return right as their LCA.
'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # O(N)
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        given this tree, let's suppose p = 6 , q = 1
        
        
                    3
                  /   \
                 5     1
                / \
               6   2
                  / \
                 7   4
        
        '''
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left != None: return left
        return right
        
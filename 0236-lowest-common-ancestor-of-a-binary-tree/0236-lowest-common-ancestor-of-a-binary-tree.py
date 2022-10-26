# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        given this tree, let's suppose p = 6 , q = 4
        
        
                    3
                  /   \
                [5]----1--------> since here we found both the left and the right to be not None, we return!  
      return 6  / \ return 4
               6   2 --------------> we now check here for whether we have a left or right to be not None.
      return null / \ return 4  
                 7   4
        
        '''
        # this is the base condition, where if we find with of the None, p or q, we 
        # return the found value.
        if root == None or root == p or root == q: 
            return root
        # we start with out dfs
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if we arrive at a node like 5 , where both left and right is not null, here we can say
        # that we've reached the LCA of both the given nodes
        if left != None and right != None: return root
        # if the left subtree contains both the nodes, we return the left
        if left != None: return left
        # and we return right if the right subtree contains both these nodes.
        return right
        


        '''
        1. Base Condition
        2. DFS
        3. Perform the operations we want
        '''
        

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(Solution().lowestCommonAncestor(root, root.left.left, root.right.left).val)
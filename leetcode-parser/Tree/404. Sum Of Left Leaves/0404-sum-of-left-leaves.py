# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root, isLeft):
            # since we have to do summation, we take a 0 as return value base condition.
            if not root:
                return 0
            if not root.left and not root.right: # Leaf Condition
                return root.val if isLeft else 0
            '''
        * Actual Computation Happens Here
            * The DFS Calls just iterate over all the elements.
            * SO make sure that whenever we have a tree computation, just make sure
            * Inside the body of the function you perform the logic inside it
            * Cause the dfs(left) + dfs(right) is just gonna be used for traversal
            '''
            return helper(root.left, True) + helper(root.right, False) 
        return helper(root,False)
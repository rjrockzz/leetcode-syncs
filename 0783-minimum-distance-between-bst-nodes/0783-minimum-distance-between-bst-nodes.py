# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        x = dfs(root)
        min_so_far = float("inf")
        for i in range(0, len(x)-1):
            min_so_far = min(min_so_far, abs(x[i] - x[i+1]))
        return min_so_far
        
        
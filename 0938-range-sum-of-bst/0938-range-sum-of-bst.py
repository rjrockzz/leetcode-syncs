# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global sum_so_far
        sum_so_far = 0
        def dfs(root):
            global sum_so_far
            if not root:
                return []
            if root.val>=low and root.val<=high:
                sum_so_far+=root.val
            return dfs(root.left) + [root.val] + dfs(root.right)
        dfs(root)
        return sum_so_far
        
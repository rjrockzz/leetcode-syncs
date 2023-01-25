# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        ans = {}
        def dfs(node, H):
            if not node: return 
            
            dfs(node.right, H + 1)
            if H not in ans: ans[H] = node.val
            dfs(node.left, H + 1)
            
        dfs(root, 0)
        return [ans[i] for i in range(len(ans))]
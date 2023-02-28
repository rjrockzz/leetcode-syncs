# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = defaultdict(int)
        res = []
        
        def dfs(node):
            if node:
                lc = dfs(node.left)
                rc = dfs(node.right)
                final_code = str(node.val) +'('+lc+')'+'('+rc+')'
                
                if hashmap.get(final_code,0) == 1:
                    res.append(node)
                hashmap[final_code] += 1
                
                return final_code
            
            return ''
        
        dfs(root)
        
        return res 
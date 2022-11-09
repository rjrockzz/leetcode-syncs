# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hashmap = defaultdict(list)
        def dfs(root, depth):
            if not root:
                return
            hashmap[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        for k, v in hashmap.items():
            hashmap[k] = sum(v)/len(v)
        return [*hashmap.values()]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def lst_builder(root):
            if not root:
                return []
            return [root.val] + lst_builder(root.left) + lst_builder(root.right)
        
        lst = lst_builder(root)
        hashmap = {}
        for i in lst:
            diff = k - i
            if diff in hashmap:
                return True
            else:
                hashmap[i] = 1+ hashmap.get(i,0)
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        result = str(root.val)
        if root.left:
            result += '(' + self.tree2str(root.left) + ')'
            if root.right:
                result += '(' + self.tree2str(root.right) + ')'
        elif root.right:
                result += '()' + '(' + self.tree2str(root.right) + ')'
        return result
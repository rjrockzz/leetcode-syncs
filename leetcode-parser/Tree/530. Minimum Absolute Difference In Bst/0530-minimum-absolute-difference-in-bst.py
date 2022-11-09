# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#     To scan the BST like a sorted array, just go through IN-ORDER traversal and keep track of the previous node evaluated.
    previous_node = -float("inf")
    result = float("inf")
    def getMinimumDifference(self, root) -> int:
        if not root:
            return None
        self.getMinimumDifference(root.left)
        self.result = min(self.result, root.val - self.previous_node) # 1 - (-inf) = 1 + inf
        self.previous_node = root.val
        self.getMinimumDifference(root.right)
        return self.result
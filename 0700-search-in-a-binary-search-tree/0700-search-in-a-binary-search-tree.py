# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Condition
        if not root:
            return
        # If we get a value == root.val, then we return that node
        if root.val==val:
            return root
        # Since a BST, we can traverse on left or right depending on the greater/lesser values
        elif root.val>val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Now we check if the root.val exists in the range [low, high]
        if root.val>high:
            return self.trimBST(root.left, low, high)
        if root.val<low:
            return self.trimBST(root.right, low, high)
        # If it exists in the range, we update our left and right!!!
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(beg, end):
            if beg > end: return None
            mid = (beg + end)//2
            root = TreeNode(nums[mid])
            root.left = helper(beg, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        
        return helper(0, len(nums) - 1)
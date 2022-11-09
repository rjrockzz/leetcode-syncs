# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
The idea is to use an in-order traversal and find the difference between the current node and the node previously checked.

Think of this question like a variation on "what is the smallest distance between any two values in a sorted array?" With a sorted array, all you do is scan through the entire array looking for the absolute minimum difference between two adjacent values since you know, when the array is sorted, that the answer can only be found between those two ADJACENT values.
'''
class Solution:
#     To scan the BST like a sorted array, just go through IN-ORDER traversal and keep track of the previous node evaluated.
    previous_node = -float("inf")
    result = float("inf")
    def minDiffInBST(self, root) -> int:
        if not root:
            return None
        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.previous_node) # 1 - (-inf) = 1 + inf
        self.previous_node = root.val
        self.minDiffInBST(root.right)
        return self.result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        # if both the left and the right are None / Non-existent, return True
        if left is None and right is None:
             return True
        # BUT if either of them is None, that means they are definitely not symmetrical
        if left is None or right is None:
            return False
        # If we get the value of the left and the right as equal, we do dfs!
        # for the left.left vs right.right
        if left.val == right.val:
            # Checking the left most and the right most values.
            outPair = self.isMirror(left.left, right.right)
            # checking the inside right (from left) and the inside left (from right)
            inPiar = self.isMirror(left.right, right.left)
            # if anyone of them is False, we return False!
            return outPair and inPiar
        else:
            # or else we just return a False and exit:)
            return False
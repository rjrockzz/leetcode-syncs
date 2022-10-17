# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
#     To scan the BST like a sorted array, just go through IN-ORDER traversal and keep track of the previous node evaluated.
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1  and not root2: # Both of the root nodes do not exist.
            return True
        elif not root1 or not root2: # Either one of root nodes does not exist.
            return False
        elif root1.val != root2.val: # If the root's values are not equal, return False
            return False        
        elif self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right):
            '''
            In this step, we finally make the descending move, we move to the left of 
            both of these trees and take the AND of both these left and the right subtrees or nodes.
            '''
            return True
        elif self.flipEquiv(root1.right,root2.left) and self.flipEquiv(root1.left,root2.right):
            '''
            In this final scenario, we actually consider the flipped elements from both of these tree
            so we take an AND of the comparison we make first with the right and left nodes of the tree and
            with the left and right of the same root, THIS IS ACTUALLY WHERE THE FLIPPING HAPPENS AND
            WE ARRIVE AT THE FINAL TEST CONDITION TO CHECK WHETHER THE TREE IF FLIP EQUIVALENT!
            '''
            return True
        return False

# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
# root1.right.left = TreeNode(6)
# root1.left.right = TreeNode(5)
# root1.left.left = TreeNode(4)
# root1.left.right.left = TreeNode(7)
# root1.left.right.right = TreeNode(8)


# root2 = TreeNode(1)
# root2.left = TreeNode(3)
# root2.right = TreeNode(2)
# root2.left.right = TreeNode(6)
# root2.right.left = TreeNode(4)
# root2.right.right = TreeNode(5)
# root2.right.right.left = TreeNode(8)
# root2.right.right.right = TreeNode(7)
# print(Solution().flipEquiv(root1,root2))

        
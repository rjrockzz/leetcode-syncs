# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    The question is composed of two requirements:

    * To remove a node, the child need to notify its parent about the child's existance.
    * To determine whether a node is a root node in the final forest, we need to know [1] whether the node is removed (which is trivial), and [2] whether its parent is removed (which requires the parent to notify the child)
    * It is very obvious that a tree problem is likely to be solved by recursion. The two components above are actually examining interviewees' understanding to the two key points of recursion:

    passing info downwards -- by arguments
    passing info upwards -- by return value
    '''
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res
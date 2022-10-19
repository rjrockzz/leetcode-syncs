# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Two solutions have the same idea:

    * Iterate the whole tree looking for the target(x and y) - either BFS or DFS
      once found, store (parent, depth) as a tuple
    * Compare the parents and depth of two nodes found and get result
    '''
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #DFS
        result = [] # Stores the (parent,depth) tuple
        
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val==y:
                result.append((parent, depth))
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)
        
        dfs(root, None, 0)
        node_x, node_y = result
        
        # just need to compare now!
        return node_x[0]!= node_y[0] and node_x[1] == node_y[1]
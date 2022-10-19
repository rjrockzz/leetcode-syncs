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
        #BFS
        result = [] # Stores the (parent,depth) tuple
        
        queue = deque([(root, None, 0)]) 
        # current_node, parent of the node, depth
        
        # start with the Vanilla BFS
        while queue:
            # An optimization to stop early if both the targets found.
            # Since once we get both the targets inside our result array, 
            # we could say that the final result can now be calculated!
            if len(result)==2:
                break
            node, parent, depth = queue.popleft()
            # if the target is found
            if node.val == x or node.val == y:
                result.append((parent,depth))
            if node.left:
                queue.append((node.left, node, depth+1))
            if node.right:
                queue.append((node.right, node, depth+1))
        node_x, node_y = result
        
        # just need to compare now!
        return node_x[0]!= node_y[0] and node_x[1] == node_y[1]
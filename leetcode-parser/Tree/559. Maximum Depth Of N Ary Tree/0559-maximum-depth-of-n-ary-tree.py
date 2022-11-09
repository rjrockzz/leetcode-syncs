"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case
        if root == None:
            return 0
        # Depth level of the tree
        depth = 0
        
        # Loops through children array
        for child in root.children:
            # Compares current depth of depth with a new level of depth 
            # Sets the biggest value to variable depth
            depth = max(depth, self.maxDepth(child))
        
        # As going deeper into the tree increases depth by 1
        print ('root ' + str(root.val) + ' depth ' + str(depth + 1))
        return depth + 1 
    
    # So for the first test case it'll look like
    # first call is the call with root 1
    # depth = 0 -> second call with child 3 -> 
    # it has 2 children so there'll be two calls from for loop
    # call with child 5 -> sets the for loop with child of 5 which is None (Null)
    # this call hits base case and returns 0
    # the same happens with child 6
    # call to child 6 from the for loop -> child of 6 is None -> returns 0
    # depth = max(0, 0) -> depth = 0
    # return to one level higher -> call to child 5 reaches return statement ->
    # depth = 1
    # call to child 6 reaches return statement and it returns 1 ->
    # current depth is 1 because child 5 set it -> max(1, 1) -> depth = 1
    # return to one more level higher
    # call to child 3 reaches return statement ->
    # depth was equal to 1 now it becomes 2 (depth + 1)
    # now it's turn to children 2 and 4 to be called
    # the story is exactly the same as with 5 and 6 only depth is now 2 ->
    # both 2 and 4 return depth 1 that's why it's rejected by max(2, 1)
    # depth remains 2
    # and finally everything returns to the very first call with root 1 
    # it reaches return statement and returns 2+1=3
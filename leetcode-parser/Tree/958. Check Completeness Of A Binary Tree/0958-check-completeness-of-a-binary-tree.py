# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        Million MERITS:
        The level-order traversal array of a complete binary tree will never have a null node in between non-null nodes. If we encounter a null node, all the following nodes should also be null, otherwise it's not complete.
        '''
        have_nulls = False
        Queue = deque([root])
        
        while Queue:
            current_node = Queue.popleft()
            if not current_node:
                # That means after this all of the nodes should be NULL, else it's not a CBT.
                have_nulls = True                
                continue  
            # After once setting the flag to True, we're now checking if the subsequent NULLS DO NO
            # EXIST!, if they do, it's not a CBT!!!
            if have_nulls: 
                return False
            Queue.append(current_node.left)
            Queue.append(current_node.right)
        return True
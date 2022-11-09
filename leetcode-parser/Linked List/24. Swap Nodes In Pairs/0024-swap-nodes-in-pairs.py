# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case if there is no head given altogether
        if not head: return head
        
        # We assign a :
        #   * prev = previous node
        #   * cur  = current node
        #.  * ans  = head.next -> since at last the node that we're gonna return is going to be the 2nd node from the intial head, which was swapped later:)
        prev, cur, ans = None, head, head.next
        # while current.next exists , we'll have a pair to swap
        while cur and cur.next:
            # take a temp kinda variable here
            adj = cur.next
            if prev: 
                prev.next = adj
            # we perform the swappings
            cur.next, adj.next = adj.next, cur
            prev, cur = cur, cur.next
        # if the head.next initially was None, we can here simply return 
        # the head as a second alternative
        return ans or head
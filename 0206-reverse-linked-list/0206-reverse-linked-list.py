# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None, head
        while curr:
            # Step 1: Keeping the track of the next node, since we're about to modify our links : \U0001f62c
            '''
            O <----------- O -----------> O 
          (prev)         (curr)       (curr.next)
             so let's assign a temp variable the value for the next node ie. curr.next
             new_node = curr.next
            '''
            next_node = curr.next
            # Step 2: Once we've saved the next node in a variable, it's safe to assume that we can
            # now proceed with changing the LINKS.Pointing our curr.next to the previous Node, 
            # THIS IS WHERE WE CHANGE OUR LINKS!!!
            '''
            O <============ O              O 
          (prev)         (curr)       (curr.next)
             so let's assign the next pointer to the Previously Occuring Node ie. prev
             # curr.next, which is a pointer to the next node, will now point to the previous node.
             curr.next = prev
            '''
            curr.next = prev
            # Step 3: Once, we've changed the links we can move forward both our pointers and the
            # we'll arrive at the same positions as we were in the Step 1, and we continue doing the rest:))
            '''
            O <----------- O -----------> O 
          (prev)         (curr)       (curr.next)
            '''
            prev = curr
            curr = next_node
        return prev
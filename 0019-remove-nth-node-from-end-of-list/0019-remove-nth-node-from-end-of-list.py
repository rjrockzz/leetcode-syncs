# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # REMOVING FROM THE END tbh.
        dummy = ListNode(0) # Sentinel Node
        dummy.next = head
        current_ptr ,deletion_ptr = dummy,dummy
        while current_ptr.next:
            if n==0:
                deletion_ptr = deletion_ptr.next
                current_ptr = current_ptr.next
            else:
                n-=1
                current_ptr = current_ptr.next
        
        deletion_ptr.next = deletion_ptr.next.next
        return dummy.next
            
            
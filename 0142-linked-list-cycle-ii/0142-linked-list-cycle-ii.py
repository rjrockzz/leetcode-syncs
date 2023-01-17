# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            # 1st part of the iteration is DONE! :)
            # We've detected the Cycle, now we need to find the 
            # Starting Points, where the cycle began.
        
        if not fast or not fast.next:
            return None
        # 2nd iteration begins => Mathematical Proof
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
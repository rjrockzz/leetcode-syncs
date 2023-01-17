# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            # Here we check for both
            #   1. If the fast initially itself isn't NULL.
            #   2. If the NEXT value to the FAST exists or NOT.
            fast = fast.next.next
            slow = slow.next
            if slow == fast: return True
        return False
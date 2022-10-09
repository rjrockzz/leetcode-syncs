# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        slow, fast = new_head, new_head
        i = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            i+=1
            if slow==fast:
                break
        else: return None
        while head!= slow:
            head, slow = head.next,slow.next
        return head
            
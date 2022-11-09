# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst = sorted(list(set(lst)))
        
        cur = dummy = ListNode(0)
        for i in lst:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
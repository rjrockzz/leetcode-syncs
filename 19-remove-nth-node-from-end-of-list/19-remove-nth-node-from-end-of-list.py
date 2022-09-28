# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        header = head
        lst = []
        while header:
            lst.append(header.val)
            header = header.next
        cur = dummy = ListNode(0)
        for x,i in enumerate(lst):
            if x!= len(lst) - n:
                cur.next = ListNode(i)
                cur = cur.next
            
        return dummy.next
            
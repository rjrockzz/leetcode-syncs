# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        mod_list,lst,i =[], [],0
        while head:
            lst.append(head.val)
            head = head.next
        
        while i+k<=len(lst):
            mod_list.extend(lst[i:i+k][::-1])
            i+=k
        mod_list.extend(lst[i:])
        
        cur = dummy = ListNode(0)
        for i in mod_list:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
            
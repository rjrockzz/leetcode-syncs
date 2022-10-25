# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_so_far = 0
        result = []
        while head:
            if head.val==0 and sum_so_far != 0:                
                result.append(sum_so_far)
                sum_so_far = 0
            sum_so_far+=head.val
            head = head.next
        curr = dummy = ListNode(0)
        for i in result:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = curr = ListNode(0)

        while l1 or l2 or carry:
            d1, d2 = 0, 0
            if l1: 
                d1 = l1.val
                l1 = l1.next
            if l2: 
                d2 = l2.val
                l2 = l2.next
            carry, digit = divmod(d1 + d2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next
              
        return head.next
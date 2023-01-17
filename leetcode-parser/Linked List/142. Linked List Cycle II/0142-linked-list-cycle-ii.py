# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can maintain a Hashmap, with our KEY as the ListNode and the VALUE as the index
        hashmap = {}
        index = 0
        while head:
            if head in hashmap:
                return head
            else:
                hashmap[head] = index
            index+=1
            head = head.next
        return None
            
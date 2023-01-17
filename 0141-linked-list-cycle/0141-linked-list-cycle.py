# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        while head:
            # Note that we're actually checking for the ListNode 
            # if it has been already visited, and not the value 
            # of the head.
            if head in hashset:
                return True
            else:
                hashset.add(head)
            head = head.next
        return False
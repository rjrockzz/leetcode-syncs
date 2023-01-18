# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel_node = ListNode(0)
        sentinel_node.next = head
        current_node = sentinel_node
        while current_node.next:
            if current_node.next.val==val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return sentinel_node.next
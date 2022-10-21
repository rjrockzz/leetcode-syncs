# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return
        # So here we're going to keep reducing our list until it is of 
        # length 0, which will be our final output.
        while len(lists) > 1:
            mergedList = []
            # we're pairing together two lists in subsequent steps
            # in order to reduce our further operations
            for i in range(0, len(lists),2):
                l1 = lists[i]
                # l2 can be out of bounds, so we're checking it here
                l2 = lists[i+1] if (i+1) <len(lists) else None
                mergedList.append(self.mergeList(l1,l2))
            lists = mergedList
        return lists[0]
    
    # The same logic for merging two linked lists:)
    def mergeList(self,l1,l2):
        dummy = ListNode()
        tail = dummy
        '''
        l1 =>   1 -> 2 -> 5
        l2 =>   4 -> 6 -> 7
        '''
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
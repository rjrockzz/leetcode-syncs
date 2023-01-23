# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Let's create the function for Reversing a Linked List.
        def reverse(head):
            curr,next_node = None, head
            while next_node:
                temp = next_node.next
                next_node.next = curr
                curr = next_node
                next_node = temp
            return curr
        # Step 2: Let's find the middle element of our Linked List.
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 3: Let's now assign the Original and the Reversed LL 
        # to a Variable for comparisons.
        
        # slow.next -> denotes the middle element of our Linked List.
        half1, half2 = head, reverse(slow.next)
        save = half2
        found = False
        # Step 4: Comparing the 2 halves now for equal elements:)
        while half1 and half2:
            if half1.val != half2.val:
                found = True
                break
            half1 = half1.next
            half2 = half2.next
        slow.next = reverse(save)
        return not found
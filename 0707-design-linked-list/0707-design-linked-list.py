class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# So we're defining the above class before proceeding^^
# We need to define our ListNode, which will actually contain 
# the new nodes that we're going to fetch.

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0) # sentinel node as the pseudo-head.

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0
        # increase the size of the LinkedList
        self.size+=1
        
        # finding the previous node of the node to be added
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        # if index is out of bounds , we return, obviously.
        if index < 0 or index >= self.size:
            return
        self.size-=1
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
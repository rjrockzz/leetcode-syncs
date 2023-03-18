# A simple implementation of the Linked List:)
class ListNode:
    def __init__(self, url):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        # The initial homepage that we're at is "homepage"
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        # A simple insertion logic in a linked list.
        new_node = ListNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        # Moving the "current" pointer to the left direction.
        while steps and self.current.prev:
            self.current = self.current.prev
            steps-=1
        return self.current.data
    
    def forward(self, steps: int) -> str:
        # Moving the "current" pointer to the right direction.
        while steps and self.current.next:
            self.current = self.current.next
            steps-=1
        return self.current.data

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
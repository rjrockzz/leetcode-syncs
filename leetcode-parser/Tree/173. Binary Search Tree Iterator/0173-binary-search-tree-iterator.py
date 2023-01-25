# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = None
        self.g = self.iterate(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.current is not self.last

    # @return an integer, the next smallest number
    def next(self):
        return next(self.g)

    def iterate(self, node):
        if node is None:
            return
        for x in self.iterate(node.left):
            yield x
        self.current = node
        yield node.val
        for x in self.iterate(node.right):
            yield x


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
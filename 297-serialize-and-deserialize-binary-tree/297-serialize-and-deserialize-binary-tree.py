# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def ser(node):
            if node:
                vals.append(str(node.val))
                ser(node.left)
                ser(node.right)
            else:
                vals.append('#')
        vals = []
        ser(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def deser():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deser()
            node.right = deser()
            return node
        vals = iter(data.split())
        return deser()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
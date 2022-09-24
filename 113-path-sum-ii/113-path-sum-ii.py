class Solution:
    def pathSum(self, root, targetSum):
        result = []
        def helper(root, path):
            nonlocal result
            if not root:
                return []
            path += [root.val]           
            if not root.left and not root.right:
                if sum(path)==targetSum:
                    result.append(path.copy())
            helper(root.left, path)
            helper(root.right, path)
            path.pop()
            return result    
        return helper(root, [])
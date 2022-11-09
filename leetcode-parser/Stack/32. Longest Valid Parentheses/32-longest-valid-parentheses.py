class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # initializing our stack with -1
        stack = [-1]
        max_value = 0
        # we're pushing the indices into the array.
        for index,s in enumerate(s):
            if s=="(":
                stack.append(index)
            else:
                stack.pop()
                if stack:
                    max_value = max(max_value,index - stack[-1])
                else:
                    stack.append(index)
        return max_value
        
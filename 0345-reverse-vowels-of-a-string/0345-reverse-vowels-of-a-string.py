class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in s:
            if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
                stack.append(i)
        for index,i in enumerate(s):
            if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
                s[index] = stack.pop()
        return "".join(s)   
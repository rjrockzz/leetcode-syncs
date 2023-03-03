class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
        for i in range(0, len(haystack) - len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1

x = Solution()
print(x.strStr("abc","c"))
class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def min_insertions(l, r):
            if l >= r:
                return 0
            elif s[l] == s[r]:
                return min_insertions(l + 1, r - 1)
            else:
                return 1 + min(min_insertions(l + 1, r), min_insertions(l, r - 1))
        
        return min_insertions(0, len(s) - 1)
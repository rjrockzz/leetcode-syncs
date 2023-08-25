class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    
        if len(s3) != len(s1) + len(s2):
            return False

        def helper(i, j, k):
            if (i, j) in seen:
                return False
            seen.add((i, j))
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if ((s1[i] == s3[k] and helper(i + 1, j, k + 1)) or
                    (s2[j] == s3[k] and helper(i, j + 1, k + 1))):
                return True
            return False

        seen = set()
        return helper(0, 0, 0)
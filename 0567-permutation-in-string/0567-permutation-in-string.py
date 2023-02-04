class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashnap = {}
        s1 = sorted(s1)
        window_size = len(s1)
        for i in range(len(s2) - window_size+1):
            if sorted(s2[i:i+window_size])==s1:
                return True
        return False
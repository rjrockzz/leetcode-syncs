class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # i-j+1
        p = sorted(p)
        result = []
        for i in range(len(s)-len(p)+1):
            if p == sorted(s[i:i+len(p)]):
                result.append(i)
        return result
                
        
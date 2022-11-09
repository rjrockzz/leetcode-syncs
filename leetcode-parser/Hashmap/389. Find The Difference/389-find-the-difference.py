class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_hashmap = Counter(t)
        for i in s:
            if i in t_hashmap:
                if t_hashmap[i]>1:
                    t_hashmap[i]-=1
                else:
                    t_hashmap.pop(i)
        return next(iter(t_hashmap))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = 1 + hashmap.get(i,0)
        for i in t:
            if i in hashmap:
                if hashmap[i]==1:
                    hashmap.pop(i)
                else:
                    hashmap[i]-=1
            else:
                return False
        return True if not hashmap else False
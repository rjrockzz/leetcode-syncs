class Solution:
    def repeatedCharacter(self, s: str) -> str:        
        hashmap = {}
        for i in s:
            hashmap[i]= 1+ hashmap.get(i,0)
            if hashmap[i]==2:
                return i
        return ""
            
            
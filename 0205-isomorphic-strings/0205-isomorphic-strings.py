class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)==1:
            return True
        i = 0 
        s_map = {}
        t_map = {}
        while i <len(s):
            if s[i] not in s_map:
                s_map[s[i]]=t[i]
                if t[i] in t_map:
                    return False
                else:
                    t_map[t[i]] = s[i]
                i+=1
            elif s_map[s[i]]==t[i] and t_map[t[i]] == s[i]:
                i+=1
            else:
                return False
        return True
                
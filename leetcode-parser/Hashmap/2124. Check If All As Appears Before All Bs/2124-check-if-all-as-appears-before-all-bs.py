class Solution:
    def checkString(self, s: str) -> bool:
        counts = Counter(s)["a"]
        for i in s:
            if i=="b":
                if counts!=0:
                    return False
                else:
                    return True
            else:
                counts-=1
        return True
            
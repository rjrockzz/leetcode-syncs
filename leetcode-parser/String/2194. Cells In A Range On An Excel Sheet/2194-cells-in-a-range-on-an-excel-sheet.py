class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        lst = s.split(":")
        low_c = lst[0][0]
        high_c = lst[1][0]
        low_r = lst[0][1]
        high_r = lst[1][1]
        res = []
        for i in range(ord(low_c), ord(high_c)+1):
            for j in range(int(low_r), int(high_r) + 1):
                res.append(chr(i)+str(j))
        return res
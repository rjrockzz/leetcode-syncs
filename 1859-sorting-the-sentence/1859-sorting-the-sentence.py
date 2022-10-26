class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split(" ")
        result = [None] * (len(lst)+1)
        for i in lst:
            result[int(i[-1])] = i[:-1]
        result.pop(0)
        return " ".join(result)
            
print(Solution().sortSentence(s = "is2 sentence4 This1 a3"))
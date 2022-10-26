class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split(" ")
        # It's important that we first create the new list, and assign the Nones
        # until the length of the 
        result = [None] * (len(lst)+1)
        for i in lst:
            # selecting the last element of list -> lst[-1]
            # selecting everything except the last element -> lst[:-1]
            result[int(i[-1])] = i[:-1]
        result.pop(0)
        return " ".join(result)
            
print(Solution().sortSentence(s = "is2 sentence4 This1 a3"))
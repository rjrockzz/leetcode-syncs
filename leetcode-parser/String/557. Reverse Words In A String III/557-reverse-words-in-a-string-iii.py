class Solution:
    def reverseWords(self, s: str) -> str:
        string = ""
        lst = s.split(" ")
        for i,n in enumerate(lst):
            lst[i]=n[::-1]
        return " ".join(lst)
            
            
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        string = ""
        while l<len(word1)  and l<len(word2):
            string+=word1[l]
            string+=word2[l]
            l+=1
        if len(word1)>len(word2):
            string+=word1[l:]
        else:
            string+=word2[l:]
        return string
        
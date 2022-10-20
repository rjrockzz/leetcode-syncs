class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        words = text.split()
        for i in text:
            if i==" ":
                spaces+=1
        if spaces==0 or len(words)==0:
            return text
        if len(words)==1:
            return words[0]+" "*spaces
        equal_spaces = spaces//(len(words)-1)
        result = ""
        for i in words:
            result+=i
            if spaces>=equal_spaces:
                result+=" "*equal_spaces
                spaces-=equal_spaces
        result+=" "*spaces
        return result
            
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        for i in patterns:
            if i in word:
                counter+=1
                
        return counter
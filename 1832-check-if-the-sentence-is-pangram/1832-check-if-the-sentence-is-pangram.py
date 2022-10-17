class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}
        for i in range(97,123):
            hashmap[chr(i)]=1
        
        for i in sentence:
            if i in hashmap:
                hashmap.pop(i)
        
        return True if not hashmap else False
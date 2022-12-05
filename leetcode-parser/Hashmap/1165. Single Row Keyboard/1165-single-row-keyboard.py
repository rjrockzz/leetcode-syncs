class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        counter = 0
        init = 0
        for index, i in enumerate(keyboard):
            hashmap[i] = index
        for w in word:
            counter+= abs(init-hashmap[w])
            init = hashmap[w]
        return counter
            
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def generate(wordList):
            for word in wordList:
                for char in word:
                    yield char
            yield None
        for c1, c2 in zip(generate(word1), generate(word2)):
            if c1 != c2:
                return False
        return True
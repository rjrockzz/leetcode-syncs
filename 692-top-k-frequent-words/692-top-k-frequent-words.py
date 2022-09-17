from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        hashmap = dict(Counter(words))
        sorted_hashmap = [*sorted(hashmap.items(), key = lambda x:(-x[1], x[0]))]
        for i in range(k):
            result.append(sorted_hashmap[i][0])
        return result
    
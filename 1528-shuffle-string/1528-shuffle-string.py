class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}
        for index, n in enumerate(indices):
            hashmap[n] = s[index]
        
        hashmap = dict(sorted(hashmap.items(), key = lambda x:x[0]))
        return "".join([*hashmap.values()])
            
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        res= []
        for i in s:
            hashmap[i] = 1 + hashmap.get(i,0)
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda x:x[1], reverse = True))
        
        for k, v in sorted_hashmap.items():
            res.extend([k]*v)
        return "".join(res)
        
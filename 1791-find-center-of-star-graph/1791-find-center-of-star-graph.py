class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {}
        for i in edges:
            for j in i:
                hashmap[j] = 1+hashmap.get(j,0)
        
        hashmap = dict(sorted(hashmap.items(), key = lambda x:x[1], reverse=True))
        return next(iter(hashmap))
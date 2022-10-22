class Solution:
    def findRestaurant(self, list1, list2):
        hashmap = {}
        hashmap_contains = {}
        res = []
        for i,n in enumerate(list1):
            hashmap[n]=i
        for i,n in enumerate(list2):
            if n in hashmap:
                hashmap_contains[n] = hashmap[n]+i
        hashmap = dict(sorted(hashmap_contains.items(),key=lambda x:x[1]))
        val = next(iter(hashmap.values()))
        for k,v in hashmap_contains.items():
            if v==val:
                res.append(k)
        return res
        
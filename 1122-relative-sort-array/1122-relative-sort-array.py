class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        for i in arr1:
            hashmap[i] = 1 + hashmap.get(i, 0)
        hashmap = dict(sorted(hashmap.items(), key = lambda x : (-x[1],x[0])))
        result = []
        for i in arr2:
            result+=[i]*hashmap[i]
            hashmap.pop(i)
        hashmap_bar = dict(sorted(hashmap.items(), key = lambda x : x[0]))
        
        for key, val in hashmap_bar.items():
            result += [key] * val
        return result
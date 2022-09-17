class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap = []
        for i in points:
            hashmap.append([i,(i[0]**2) + (i[1]**2)])
        hashmap.sort(key = lambda x : x[1])
        return [list(keys[0]) for keys in hashmap][:k]
            
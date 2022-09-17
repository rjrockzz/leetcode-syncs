class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap = []
        heap = answer = []
        for i in points:
            hashmap.append([((i[0]**2) + (i[1]**2)), i])
        heapq.heapify(hashmap)
        return [heapq.heappop(hashmap)[1] for _ in range(k)]
            
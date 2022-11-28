class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix = [j for sub in matrix for j in sub]
        heapq.heapify(matrix)
        i = 0
        while i <k-1:
            heapq.heappop(matrix)
            i+=1
        return matrix[0]
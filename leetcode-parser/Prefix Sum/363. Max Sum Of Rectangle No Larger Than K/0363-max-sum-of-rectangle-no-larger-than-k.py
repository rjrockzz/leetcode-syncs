class Solution:
    # Keep the row prefix sums for different columns and rows
    # Then for each col pair i and j, add the row prefix sums row by row to the cumulative sum
    # Previously seen cumulative sum was saved as in a sorted array
    # We therefore binary search on this sorted array for cumu_sum - K. If we see an exact match, the result is k
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        row_prefix = [[0 for i in range(n+1)]]
        for row in matrix:
            current = [0]
            for j in range(n):
                current.append(row[j] + current[-1])
            row_prefix.append(current)
        #print(row_prefix)
        
        result = - float('inf')
        # sum between columns i and j
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                arr = []
                for r in range(0, m + 1):
                    if r == 0:
                        arr.append(0)
                        cumu_sum = 0
                    else:
                        cumu_sum += row_prefix[r][j] - row_prefix[r][i]
                        x = bisect.bisect_left(arr, cumu_sum - k)
                        if x < len(arr):
                            if arr[x] == cumu_sum - k:
                                return k
                            else:
                                result = max(result, cumu_sum - arr[x])
                        bisect.insort(arr, cumu_sum)
                        #print(r, i, j, arr)
        return result
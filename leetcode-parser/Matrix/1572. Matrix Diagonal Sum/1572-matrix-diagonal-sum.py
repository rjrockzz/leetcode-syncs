'''
Clean Python solution showcasing a One-Pass algorithm to perform a sum over both diagonals. At the end of the process, we check if the square matrix has an "odd" size. If this happened, we need to subtract the middle element which was summed twice. Otherwise, everything is fine (it's easy to prove/visualize that for matrices of even size the diagonals don't intersect, so nothing gets repeated while summing).

Time Complexity: O(N), where "N" is the matrix size.
Space Complexity: O(1), since we only use scalar variables.
Edge Case Handling: O(1) Time/Space Complexity (We correct our results only once. The O(n) loop isn't affected at all).
'''
# We can find whether a number is odd or even also by taking an "&1" operation:)
# Python
class Solution:
    def diagonalSum(self, A):
        n   = len(A)
        res = 0
        for i in range(n):
            res += A[i][i] + A[i][n-1-i]
        # x: Index of Element Repeated (when n is Odd)
        x = (n-1)//2
        return res - A[x][x] if n%2 else res
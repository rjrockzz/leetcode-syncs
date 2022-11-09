class Solution:
    def projectionArea(self, grid):
        top = sum(v != 0 for row in grid for v in row)
        front = sum(max(row) for row in grid)
        side = sum(max(row[j] for row in grid) for j in range(len(grid)))
        return top + front + side
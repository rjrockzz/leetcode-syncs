class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns, count = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
    def dfs(self,grid, i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j] = "#"
        self.dfs(grid, i+1,j)
        self.dfs(grid, i-1,j)
        self.dfs(grid, i,j+1)
        self.dfs(grid, i,j-1)
        
        
        
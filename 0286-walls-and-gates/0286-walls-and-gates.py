class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        n, m = len(rooms), len(rooms) and len(rooms[0])
        q = [(i,j) for i in range(n) for j in range(m) if not rooms[i][j]]
        for i, j in q:
            for x, y in ((i-1,j), (i+1,j),(i,j-1),(i,j+1)):
                if 0 <= x < n and 0 <= y < m and rooms[x][y] == 2**31-1:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))
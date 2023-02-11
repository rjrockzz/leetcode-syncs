from collections import deque

class Solution:
    class Node:
        def __init__(self, number):
            self.number = number
            self.blueCities = []
            self.redCities = []
    
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        hashMap = {}
        for i in range(n):
            hashMap[i] = Solution.Node(i)
            
        for redEdge in redEdges:
            hashMap[redEdge[0]].redCities.append(redEdge[1])
        
        for blueEdge in blueEdges:
            hashMap[blueEdge[0]].blueCities.append(blueEdge[1])
        
        ans = [-1] * n
        visit = [[False, False] for _ in range(n)]
        q = deque([[0, 0, -1]])
        ans[0] = 0
        visit[0][0] = visit[0][1] = True
        
        while q:
            element = q.popleft()
            nodeNumber, steps, prevColor = element
            
            for neighbor in hashMap[nodeNumber].redCities:
                if not visit[neighbor][0] and prevColor != 0:
                    if ans[neighbor] == -1:
                        ans[neighbor] = steps + 1
                    visit[neighbor][0] = True
                    q.append([neighbor, steps + 1, 0])
            
            for neighbor in hashMap[nodeNumber].blueCities:
                if not visit[neighbor][1] and prevColor != 1:
                    if ans[neighbor] == -1:
                        ans[neighbor] = steps + 1
                    visit[neighbor][1] = True
                    q.append([neighbor, steps + 1, 1])
        
        return ans
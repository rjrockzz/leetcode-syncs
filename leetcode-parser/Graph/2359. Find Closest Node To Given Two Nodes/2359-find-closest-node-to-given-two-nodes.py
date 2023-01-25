class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d1 = [float('inf') for _ in range(len(edges))]
        d2 = [float('inf') for _ in range(len(edges))]
        def bfs(st,dist):
            visited = set([st])
            queue = [(st,0)]
            while queue:
                node,distance = queue.pop(0)
                dist[node] = distance
                if edges[node] != -1:
                    if edges[node] not in visited:
                        visited.add(edges[node])
                        queue.append((edges[node],distance+1))
        bfs(node1,d1)
        bfs(node2,d2)
        self.mini = float('inf')
        final_node = -1
        for i in range(len(d1)):
            if max(d1[i],d2[i]) < self.mini:
                self.mini = max(d1[i],d2[i])
                final_node = i
                
        return final_node 
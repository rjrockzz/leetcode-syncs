class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(g,c,vis,res):
            vis[c] = True
            for adj in g[c]:
                if not vis[adj]:
                    dfs(g,adj,vis,res)
                #adj can be visited by current vertex so we dont have to add adj in res
                elif adj in res:res.remove(adj)
        
        #Make a adjecency list
        g = collections.defaultdict(list)
        for e in edges:
            u,v = e
            g[u].append(v)
            
        
        res = set()
        vis = [False]*n
        for i in range(n):
            if not vis[i]:
                dfs(g,i,vis,res)
				#add vertex from which we start traversing
                res.add(i)
        return list(res)
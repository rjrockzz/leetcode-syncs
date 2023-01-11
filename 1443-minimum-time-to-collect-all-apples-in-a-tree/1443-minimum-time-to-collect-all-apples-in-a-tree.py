'''Just like performing Kahn's algorithm of topological sort on a tree.
Sum degrees of each node first, then peel the tree from those nodes whose degree is 1.
Once there is no appropriate node can be removed, just return sum of all degrees.
Note that we shouldn't peel node 0 so let hasApple[0] = True at beginning.
Time: O(N)
Each edge will be visited at most twice, and there will be n - 1 edges because it's a tree.
Space: O(N)
'''
import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasApple[0], degree = True, [0] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        queue = collections.deque(v for v in range(n) if degree[v] == 1)
        while queue:
            u = queue.popleft()
            if hasApple[u]: continue
            for v in graph[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                    degree[u] -= 1
                    if degree[v] == 1:
                        queue.append(v)
        return sum(degree)
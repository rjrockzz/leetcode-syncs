class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cached_dist, visited = collections.defaultdict(int), set()
        n, max_cycle_len = len(edges), -1
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)

            # Scope the distances cache per each traversal.
            cached_dist.clear()
            cached_dist[i] = 1
            current, next = i, edges[i]
            while next != -1:
                if next not in visited:
                    cached_dist[next] = cached_dist[current] + 1
                else:
                    # Cycle found. Key is to check whether the already visited node
                    # is part of the current traversal. Otherwise we may compute the length
                    # of a path instead of a cycle.
                    max_cycle_len = (max(max_cycle_len,
                                         cached_dist[current] - cached_dist[next] + 1)
                                     if cached_dist[next] else max_cycle_len)
                    break
                visited.add(next)
                current, next = next, edges[next]

        return max_cycle_len
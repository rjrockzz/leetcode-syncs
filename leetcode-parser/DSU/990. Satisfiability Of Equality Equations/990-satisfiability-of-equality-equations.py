class Solution:     # Here's the plan:
                    #   1) We make an undirected graph in which the nodes are integers
                    #      (as lower-case letters) and each edge connects integers
                    #      that are equal.
                    #   2) We use a union-find process to determine the connected graphs
                    #   3) We keep track of the pairs (a,b) such that a =! b. If the any
                    #      such pair are in the same connected graph, then return False,
                    #      otherwise return True.
    def equationsPossible(self, equations: List[str]) -> bool:
        parent, diff = {}, []

        def find(x):
            if x not in parent: return x
            else: return find(parent[x])

        for s in equations:                 # <-- 1)
            a, b = s[0], s[3]

            if s[1]== "=":                  # <-- 2)
                x, y = find(a), find(b)
                if x!=y:
                    parent[y] = x
            else:    
                diff.append((a,b))          # <-- 3)

        return all(find(a)!=find(b) for a, b in diff)
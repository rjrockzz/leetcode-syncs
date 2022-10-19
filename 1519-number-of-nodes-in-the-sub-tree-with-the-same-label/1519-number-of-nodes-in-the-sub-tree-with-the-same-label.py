import collections
class Solution:
    '''
    In the question it does not specify whether it is a binary tree or not so we proceed with using the graphs concepts.
    '''
    def countSubTrees(self, n: int, edges, labels):
        graph = collections.defaultdict(list)
        
        # since the edges are provided as a list of list with 2 elements, the start and end.
        # let's suppose that the edge list that we have is [[0,1],[1,2],[0,3]]
        # so the graph dict will be constructed as follows
        for u, v in edges:
            # undirected
            graph[u].append(v)
            graph[v].append(u)
        
    # And the graph dict is gonna look like {0:[1, 3],1:[0, 2],2:[1],3:[0]} 
    # The lenght of the graph will be the number of unique points in the edges (nodes)
        result = [0] * n
        # initialize the result array with 0's
        def dfs(index, parents):
            counts = collections.Counter()
            # We calculate for all the edges in the graph so something like
            # graph[0], graph[1], graph[2], graph[3] since we have 0 -> 3 inclusive nodes.
            for edge in graph[index]:
                # We're now inside the values of our dict graph, where it reps the number of connected nodes 
                # to that particular node, now we check if we don't have the parent as the edge inside the 
                # list of values, since we have to move downwards to calculate the number of nodes, having the same label.
                if edge!=parents:
                    counts+=dfs(edge, index) # we now update the edge and parent and send it t0 be calcuated recursively:)
            counts[labels[index]] +=1
            result[index] = counts[labels[index]]
            return counts
        dfs(0,-1) # starting from index 0, the parent as -1 or None :)
        return result

# print(Solution().countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
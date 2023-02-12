class Solution:
    import math
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        network = defaultdict(lambda:set())
        for rd in roads:
            network[rd[0]].add(rd[1])
            network[rd[1]].add(rd[0])
            
        def dfs(node,visited):
            
            visited.add(node)
            cost_fuel = 0
            num_of_people = 1
            
            for neighbour in network[node]:
                
                if neighbour not in visited:
                    node_fuel, nums = dfs(neighbour,visited)
                    num_of_people += nums 
                    cost_fuel += node_fuel + math.ceil(nums/seats)
                    
            return cost_fuel, num_of_people
        
        res,irrev = dfs(0,set())
        return res 
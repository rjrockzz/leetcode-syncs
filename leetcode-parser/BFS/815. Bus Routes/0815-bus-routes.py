class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Since we have to visit each stops using the buses also see
        # WE SHOULD NOT USE routes instead of the buses for BFS because of the constraints
        # Using BFS is kind of the go-to here since we have to find the minimum
        # number of buses, that is the shortest path to reach a particular stop.
        
        # our base condition can be to simply return the stop if we're already at the 
        # start == stop
        if source==target:
            return 0
        
        routes_to_bus = collections.defaultdict(set)
        # we're now creating a mapping of the routes -> bus, since now we will 
        # be performing our BFS on the buses instead of the stops due to the constraints.
        for index,i in enumerate(routes):
            for j in i:
                routes_to_bus[j].add(index)
        # Now since we're moving forward to our BFS, let's initialize 
        # some of our variables.
        seen_stops = set()
        seen_buses = set()
        queue = deque([(source, 0)])
        
        # now we can proceed for our bfs
        while queue:
            stop, bus_count = queue.popleft()
            if stop==target:
                return bus_count
            
            for bus_number in routes_to_bus[stop]: # traversing through the buses
                if bus_number not in seen_buses:
                    seen_buses.add(bus_number)
                    # now we traverse the stops created by the buses
                    for stop_of_the_bus_number in routes[bus_number]:
                        if stop_of_the_bus_number not in seen_stops:
                            seen_stops.add(stop_of_the_bus_number)
                            queue.append((stop_of_the_bus_number, bus_count+1))
        return -1
            
                
        
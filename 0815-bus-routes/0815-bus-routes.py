'''
Explanation:
* The first part loop on routes and record stop to routes mapping in to_route.
* The second part is general bfs. Take a stop from queue and find all connected route.
* The hashset seen record all visited stops and we won't check a stop for twice.
* We can also use a hashset to record all visited routes, or just clear a route after visit.
'''
import collections
class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        # mapping of stops to the bus
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i) 
        '''
        final result is like let's suppose for bus 0 the routes were like [1,2,7], so the to_routes mapping comes out to be (defaultdict with set as the default type) {1 : {0}, 2: {0}, 7:{0}} and for the bus 1 it will be {1 : {0}, 2: {0},3:{1},6:{1}, 7:{0,1}}
        '''
        bfs = [(source, 0)]
        '''
        initially we intitialise it to [(1, 0)], where 1 is the source and the 0 is the bus to be taken, init bus = 0 that means we haven't boarded any bus as of yet.
        '''
        seen = set([source]) # since we're already starting with the source, we can mark it as visited.
        for stop, bus in bfs: # intially stop = 1, bus = 0
            if stop == target: # stopping condition.
                return bus
            for i in to_routes[stop]: # stop initially 1, ie. to_routes[stop] = 0
                for j in routes[i]: # now traversing through all the routes for that particular bus, since now we know that the bus will definitely stop at that particular stop, so we carry on visiting the routes it will now further take in the course of the journey.

                    if j not in seen: # we check if we have already visited that stop before, it means it's of no use visiting the same stop again in the further steps.
                        bfs.append((j, bus+1)) 
                        seen.add(j)
                # we mark this as empty list as soon as we have visited using a particular bus point.
                routes[i] = []                 
        return -1
x = Solution()
print(x.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
'''
We have to go the furthest direction, right?
If the next building is "taller", in that case, we can either:
* use h[i+1] - h[i] bricks
* or use a ladder
We need to go the furthest building optimally...
                
                             ___
                            |   |
                         ___|   |  
        climb here ---->|   |   |___
                     ___|   |   |   |
                    |   |   |   |   |
                ____|___|___|___|___|___
from the initial intuition, we can say that firstly, we can exhaust off all our bricks before we start using the ladders
'''

from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
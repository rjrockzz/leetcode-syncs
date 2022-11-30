'''
Since,we need to always get the minimum possible cost of the stick, we will be heapifying the given array, and get the minimum element always, until the length of the heap is 1.
'''
import heapq
from typing import List
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) != 1:
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            cost += stick_1 + stick_2
            heapq.heappush(sticks, stick_1 + stick_2)
        return cost
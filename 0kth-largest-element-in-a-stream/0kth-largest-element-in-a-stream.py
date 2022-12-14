class KthLargest:
    # Always maintaining the MIN heap with only K elements, always be at root position.
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # if after adding new items causes the heap size to increase beyond k,
        # we then pop out the smallest element.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
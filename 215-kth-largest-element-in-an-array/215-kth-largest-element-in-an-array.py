class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        
        def adders(num):
            nonlocal heap
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        for num in nums:
            adders(num)
    
        return heap[0]
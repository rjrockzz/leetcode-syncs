class Solution:
    def findKthLargest(self, nums, k):
        ans = 0
        nums_rev = [-1*i for i in nums]
        heapq.heapify(nums_rev)
        for i in range(k):
            ans = heapq.heappop(nums_rev)
        
        return -ans
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # step 1: sort the nums, O(logn)
        nums.sort()
        # step 2: calculate the running sum of the nums, O(n)
        self.running_sum = []
        rs = 0
        for num in nums:
            rs += num
            self.running_sum.append(rs)
        
        # step 3: binary search the running sum value that is less than or equal to each query
        ans = []
        for q in queries:
            rs_idx = self.binarySearch(q)
            ans.append(rs_idx + 1)
        return ans
    
        
    def binarySearch(self, q):
        start = 0
        end = len(self.running_sum) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.running_sum[mid] == q:
                return mid
            elif self.running_sum[mid] < q:
                start = mid + 1
            else:
                end = mid - 1
        # make sure that the returned index points to the less-than-or-equal-to value
        if self.running_sum[mid] > q:
            return mid - 1
        return mid
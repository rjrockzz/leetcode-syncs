class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        sum_required = sum(nums)//2
        n = len(nums)
        t = [[-1 for i in range(sum_required+1)] for j in range(n+1)]
        def dp(nums, n, sum_required):
            if sum_required == 0:
                return True
            if n == 0 and sum_required != 0:
                return False
            if t[n][sum_required]!=-1:
                return t[n][sum_required]
            t[n][sum_required] = dp(nums, n-1, sum_required-nums[n-1]) or dp(nums, n-1, sum_required)
            return t[n][sum_required]
        
        return dp(nums, n,sum_required)
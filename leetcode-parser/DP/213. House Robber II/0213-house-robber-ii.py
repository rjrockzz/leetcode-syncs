class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob0(nums):
            global_max = curmax = 0
            for i in range(len(nums)-1): # from 0 -> n-1
                t = curmax
                curmax = max(global_max + nums[i], curmax)
                global_max = t
            return curmax
        
        def rob1(nums):
            global_max = curmax = 0 
            for i in range(1,len(nums)): # from 1 -> n
                t = curmax
                curmax = max(global_max + nums[i], curmax)
                global_max = t
            return curmax
        return max(rob0(nums), rob1(nums))
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_so_far =prev =  0
        for i in range(len(nums)):
            if prev==0:
                prev = sums = nums[i]
                continue
            if nums[i]>prev:
                sums+=nums[i]
                max_so_far = max(max_so_far,sums)
            else:
                sums= nums[i]
            prev = nums[i]
        return max_so_far if max_so_far>max(nums) else max(nums)
                
            
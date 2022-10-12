class Solution:
    def largestPerimeter(self, nums) -> int:
        max_perimeter = 0
        nums.sort(reverse=True)
        for i in range(0,len(nums)-2):
            if nums[i+0] + nums[i+1] <= nums[i+2] or nums[i+1] + nums[i+2] <= nums[i+0] or nums[i+2] + nums[i+0] <= nums[i+1]:
                continue
            else:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
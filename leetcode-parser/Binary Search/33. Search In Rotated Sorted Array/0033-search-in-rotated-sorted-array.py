class Solution:
    def search(self, nums, target: int) -> int:
        
        prev = -1
        prev_element = float("-inf")
        index_rot = 0
        res = nums.copy()
        for index, i in enumerate(nums):
            if i > prev_element:
                prev_element = i
            else:
                res = nums[index:] + nums[:index]
                index_rot = index
                break
        
        left, right = 0, len(nums) - 1
        while left<= right:
            mid = left + (right-left)//2
            if res[mid]==target:
                return (mid+index_rot)%len(nums)
            elif res[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return -1
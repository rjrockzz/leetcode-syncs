class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        def bin_search(l,r,target, nums):
            if l>r:
                return -1
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                return bin_search(l,mid-1,target,nums)
            else:
                return bin_search(mid+1, r, target, nums) 
        x = bin_search(left,right, target, nums)
        return x
# x = Solution()
# print(x.search(nums = [-1,0,3,5,9,12], target = 9))
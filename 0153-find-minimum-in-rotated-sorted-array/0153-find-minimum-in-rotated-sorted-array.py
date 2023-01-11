class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            # Left rotated:
            if nums[mid] > nums[right]:
                left = mid+1
            # Right rotated
            else:
                right = mid
        return nums[left]
            
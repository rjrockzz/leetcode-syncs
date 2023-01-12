from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Array's sorted in Non-Descending Order
        # If no target found, we return [-1, -1]
        if len(nums)==0:
            return [-1, -1]
        
        def searchLow(nums, target):
            left, right = 0, len(nums) - 1
            while left<right:
                mid = (left + right)//2
                if nums[mid]==target and nums[mid]!= nums[mid-1]:
                    return mid
                elif nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            return left if nums[left]==target else -1
        
        def searchHigh(nums, target):
            left, right = 0, len(nums) - 1
            while left<right:
                mid = (left + right)//2
                if nums[mid]==target and nums[mid]!= nums[mid+1]:
                    return mid
                elif nums[mid]<=target:
                    left = mid+1                    
                else:
                    right = mid
            return right if nums[right]==target else -1 
        return [searchLow(nums, target), searchHigh(nums, target)]
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # At every step we're gonna check the left and the right neighbour
        # We're gonna add a left and right infinity as mentioned in the problem
        nums = [float('-inf')] + nums + [float('-inf')]
        
        for i in range(1, len(nums)-1):
            if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
                return i-1
        return -1
class Solution:
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right): 
            return self.findKthLargest(right, k)
        elif len(right) < k <= len(right) + len(equal): 
            return equal[0]
        else: 
            return self.findKthLargest(left, k - len(right) - len(equal))
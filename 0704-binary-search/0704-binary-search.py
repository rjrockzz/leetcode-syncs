class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since our array is already sorted , let's run the Binary Search
        left, right = 0, len(nums)-1
        
        while left<=right:
            # Always define your mid inside the while statement
            mid = (left+right)//2
            if target== nums[mid]:
                return mid
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return -1
                
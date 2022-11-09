class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_total = sum(nums)
        sum_right = sum_total
        sum_left = 0
        for index,i in enumerate(nums):
            sum_right-=i
            if sum_right==sum_left:
                return index
            sum_left+=i
        return -1
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        builder_odd = []
        builder_even = []
        for num in nums:
            if num%2==0:
                builder_even.append(num)
            else:
                builder_odd.append(num)
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = builder_even.pop(0)
            else:
                nums[i] = builder_odd.pop(0)
        return nums
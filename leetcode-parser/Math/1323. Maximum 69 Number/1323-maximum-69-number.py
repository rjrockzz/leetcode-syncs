class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = list(str(num))
        for index, i in enumerate(nums):
            if i=="6":
                nums[index] = "9"
                return int("".join(nums))
        return num
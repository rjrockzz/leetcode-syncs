class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                x+=1
        return 1 if x%2==0 else -1
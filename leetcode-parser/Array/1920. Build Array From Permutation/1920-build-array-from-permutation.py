class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i,n in enumerate(nums):
            ans.append(nums[n])
        return ans
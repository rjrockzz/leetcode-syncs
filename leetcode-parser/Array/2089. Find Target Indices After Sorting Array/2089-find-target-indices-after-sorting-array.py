class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for index, i in enumerate(nums):
            if i==target:
                result.append(index)
        return result
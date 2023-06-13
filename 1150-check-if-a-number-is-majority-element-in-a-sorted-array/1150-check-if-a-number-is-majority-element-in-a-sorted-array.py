class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start = bisect_left(nums, target)
        return start + (N := len(nums)) // 2 < N and nums[start + N // 2] == target
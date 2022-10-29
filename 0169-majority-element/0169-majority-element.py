class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
            if hashmap[i] > majority:
                return i
        
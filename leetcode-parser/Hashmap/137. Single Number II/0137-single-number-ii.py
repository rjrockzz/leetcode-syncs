class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        hashmap = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1])}
        return next(iter(hashmap))
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = 1 + hashmap.get(i,0)
        return False
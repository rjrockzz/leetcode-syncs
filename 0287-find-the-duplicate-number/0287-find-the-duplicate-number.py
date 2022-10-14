class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setmap = set()
        for i in nums:
            if i in setmap:
                return i
            else:
                setmap.add(i)
        return 0
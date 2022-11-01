from collections import Counter
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        nums.sort()
        for i in nums:
            if i<0:
                if -i in nums_counter:
                    return -i
        return -1
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        for i in range(len(strs[0])):
            str_builder = ""
            for j in strs:
                str_builder+=j[i]
            if str_builder != "".join(sorted(str_builder)):
                # sorted returns the list of elements, so we need to join it
                counter+=1
        return counter
x = Solution().minDeletionSize(["cba","daf","ghi"])
print(x)
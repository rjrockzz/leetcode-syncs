# Revisit
from typing import List, Tuple
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        shortest = sorted(strs, key = len)[0]
        for i in range(len(shortest)):
            curr = shortest[i]
            for j in strs:
                if j[i]==curr:
                    continue
                else:
                    return final
            final+=curr
        return final
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(set(str(num)))==1:
            return True
        return True if num==int(str((str(num)[::-1].lstrip("0"))[::-1])) else False
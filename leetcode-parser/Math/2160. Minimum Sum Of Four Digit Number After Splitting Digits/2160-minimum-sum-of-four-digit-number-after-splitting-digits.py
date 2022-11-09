class Solution:
    def minimumSum(self, num: int) -> int:
        a = sorted(str(num))
        return int(a[0] + a[2]) + int(a[1] + a[3])
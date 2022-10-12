# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n-1
        left = 0
        while left <= right:
            mid = left + (right-left)//2
            if isBadVersion(mid)==False:
                left = mid+1
            else:
                right = mid-1
        return left # or we can also return right, any of them will work since it ends at left==right, and we are finding the index of the element we want to search
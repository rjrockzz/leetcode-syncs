'''
        We're given array nums
        n positive integerss
        computed the sum of all-non empty continouos subarrays
        and then sorted them in a non-decreasing order, creating a 
        new array of n * (n+1) /2 numbers
        
'''
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        n = len(prefix)
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                total = prefix[i] - prefix[j]
                ans.append(total)

        ans.sort()
        return sum(ans[left-1:right])% 1_000_000_007
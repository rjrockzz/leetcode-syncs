class Solution:
    def maximumScore(self, nums, muls):
        # let dp[i][j] represents pick i elements from left and pick j from right from nums
        # dp[i][j] = Max(dp[i-1][j] + muls[i+j-1] * nums[i-1], dp[i][j-1] + muls[i+j-1] * nums[n-j])
        n, m = len(nums), len(muls)
        dp = [[0] * (m+1) for _ in range(m+1)]
        res = float("-inf")
        for i in range(0, m+1):
            for j in range(0, m-i+1):
                if i == 0 and j == 0: 
                    continue
                l, r = float("-inf"), float("-inf")
                if i > 0: l = dp[i-1][j] + muls[i+j-1] * nums[i-1] # pick left
                if j > 0: r = dp[i][j-1] + muls[i+j-1] * nums[n-j] # pick right
                dp[i][j] = max(l, r)
                if i + j == m:
                    res = max(res, dp[i][j])
        return res
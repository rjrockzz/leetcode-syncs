from functools import lru_cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left, right):
            if left >= right:
                return 0
            ans = float("inf")
            for pick in range(left, right + 1):
                leftCost = dp(left, pick - 1) + pick  # Cost on the left side, if pivot is not a secret number
                rightCost = dp(pick + 1, right) + pick  # Cost on the right side, if pivot is not a secret number
                cost = max(leftCost, rightCost)  # The cost is the maximum between the left side and the right side
                ans = min(ans, cost)  # Choose pivot which will cause minimum cost
            return ans

        return dp(1, n)

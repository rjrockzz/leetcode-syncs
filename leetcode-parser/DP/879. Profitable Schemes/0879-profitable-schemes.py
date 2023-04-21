class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        @lru_cache(None)
        def dfs(i,crntpro,people):
            if i>=len(group):
                return crntpro>=minProfit
            ways=0   
            if people+group[i]<=n:
                ways+=dfs(i+1,min(minProfit,crntpro+profit[i]),people+group[i])
            ways+=dfs(i+1,crntpro,people)
            return ways
        return dfs(0,0,0)%(10**9+7)
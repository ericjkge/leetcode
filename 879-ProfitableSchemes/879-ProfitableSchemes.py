# Last updated: 8/20/2025, 12:40:24 AM
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(index, used, prof): # num ways using crimes[index:] after using used members and already earned prof
            if used > n:
                return 0
            if index == len(group):
                return 1 if prof >= minProfit and used <= n else 0
            
            skip = dp(index + 1, used, prof)
            take = dp(index + 1, used + group[index], min(minProfit, prof + profit[index]))
            return (skip + take) % MOD
        
        return dp(0, 0, 0)
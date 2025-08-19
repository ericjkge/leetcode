# Last updated: 8/19/2025, 11:47:18 PM
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones) 

        @cache
        def dp(i, j):
            if j == n:
                return i if i >= 0 else float("inf")
            
            return min(dp(i + stones[j], j + 1), dp(i - stones[j], j + 1))

        return dp(0, 0)
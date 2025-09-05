# Last updated: 9/5/2025, 9:19:34 AM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i): # min way to get amount i
            if i == 0:
                return 0
            
            if i < 0:
                return float("inf")

            ways = float("inf")
            for c in coins:
                ways = min(ways, 1 + dp(i - c))
            return ways

        ans = dp(amount)
        return ans if ans != float("inf") else -1


        # Alternative: backtracking TLE but logically correct
        
        # self.ans = float("inf")
        # n = len(coins)

        # def backtrack(total, length):
        #     if total > amount:
        #         return

        #     if total == amount:
        #         self.ans = min(self.ans, length)
        #         return
            
        #     for c in coins:
        #         backtrack(total + c, length + 1)
        
        # backtrack(0, 0)
        # return self.ans if self.ans != float("inf") else -1
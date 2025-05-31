# Last updated: 5/31/2025, 3:27:17 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i < 0:
                return -1
            
            if i == 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            result = float("inf")
            for c in coins:
                if i-c >= 0:
                    result = min(result, dp(i-c) + 1)
            
            memo[i] = result
            return memo[i]
        
        memo = {}
        ans = dp(amount)
        return -1 if ans == float("inf") else ans
# Last updated: 5/31/2025, 3:27:11 PM
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0]] * (n+1)
     
        for i in range(n-1, -1, -1):
            dp[i][0] = max(dp[i+1][0], -prices[i]+dp[i+1][1])
            dp[i][1] = max(dp[i+1][1], prices[i]-fee+dp[i+1][0])
        
        return dp[0][0]
        
        
#         @cache
#         def dp(i, holding): # max profit up to stock i w. boolean holding
#             if i == len(prices):
#                 return 0
            
#             ans = dp(i+1, holding) #skip stock i
#             if holding:
#                 ans = max(ans, prices[i] - fee + dp(i+1, False))
#             else:
#                 ans = max(ans, -prices[i] + dp(i+1, True))
            
#             return ans
        
#         return dp(0, False)
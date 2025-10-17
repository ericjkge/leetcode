# Last updated: 10/17/2025, 11:21:14 AM
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i): # No. of decodings for s[i:]
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            
            res = dp(i + 1)
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                res += dp(i + 2)
            
            return res
        
        return dp(0)

# NOTE: dp[i - 1] is num ways to decode up to prev char (inclusive), s[i - 1] is current char. think about transition as adding up both possible ways, since for one you can just append the current char and for two you just append prev and current char
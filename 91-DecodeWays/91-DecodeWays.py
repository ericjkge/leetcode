# Last updated: 10/17/2025, 11:32:38 AM
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i):
            if i == n:
                return 1
            
            if s[i] == "0":
                return 0
            
            res = dp(i + 1)
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                res += dp(i + 2)
            return res
        
        return dp(0)

# Last updated: 8/22/2025, 12:58:42 AM
class Solution:
    def strangePrinter(self, s: str) -> int:
        t = []
        for char in s:
            if not t or t[-1] != char:
                t.append(char)
        
        s = "".join(t)
        n = len(s)

        @cache
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            
            res = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, dp(i + 1, k - 1) + dp(k, j))
            return res

        return dp(0, n - 1)
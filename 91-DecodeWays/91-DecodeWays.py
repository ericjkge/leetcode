# Last updated: 11/28/2025, 1:28:47 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4
5        @cache
6        def dp(i):
7            if i == n:
8                return 1
9
10            if s[i] == "0":
11                return 0
12            
13            res = dp(i + 1)
14
15            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
16                res += dp(i + 2)
17
18            return res
19
20        return dp(0)
21
22        # n = len(s)
23
24        # @cache
25        # def dp(i):
26        #     if i == n:
27        #         return 1
28            
29        #     if s[i] == "0":
30        #         return 0
31            
32        #     res = dp(i + 1)
33        #     if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
34        #         res += dp(i + 2)
35        #     return res
36        
37        # return dp(0)
38
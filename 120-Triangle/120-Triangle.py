# Last updated: 1/13/2026, 11:49:42 PM
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        n = len(triangle)
4
5        @cache
6        def dp(i, j): # array, index
7            if i == n:
8                return 0
9
10            if j < 0 or j == len(triangle[i]):
11                return float("inf")
12            
13            return triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
14        
15        return dp(0, 0)
16
17
18"""
19   -1
20  3.  2
21-3. 1. -1
22"""
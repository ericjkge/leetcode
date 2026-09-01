# Last updated: 9/1/2026, 6:26:40 AM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        seen = set()
5        
6        def dfs(c):
7            seen.add(c)
8            for i in range(n):
9                if c != i and isConnected[c][i] and i not in seen:
10                    dfs(i)
11
12        count = 0
13        for i in range(n):
14            if i not in seen:
15                count += 1
16                dfs(i)
17        
18        return count
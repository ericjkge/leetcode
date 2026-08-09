# Last updated: 8/8/2026, 11:44:24 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        seen = set()
5
6        def dfs(i):
7            seen.add(i)
8            for j in range(n):
9                if isConnected[i][j] and j not in seen:
10                    dfs(j)
11    
12        count = 0
13        for i in range(n):
14            if i not in seen:
15                count += 1
16                dfs(i)
17            
18        return count
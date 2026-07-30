# Last updated: 7/29/2026, 9:22:32 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4
5        def dfs(node):
6            seen.add(node)
7            for neighbor in range(n):
8                if isConnected[node][neighbor] and neighbor not in seen:
9                    dfs(neighbor)
10
11        seen = set()
12        count = 0
13        for i in range(n):
14            if i not in seen:
15
16                dfs(i)
17                count += 1
18        
19        return count
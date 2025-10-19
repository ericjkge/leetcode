# Last updated: 10/19/2025, 9:00:17 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        seen = set()

        def dfs(i):
            for j in range(0, len(isConnected)):
                if isConnected[i][j]:
                    if j not in seen:
                        seen.add(i)
                        dfs(j)
        
        for i in range(len(isConnected)):
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans += 1

        return ans
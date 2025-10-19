# Last updated: 10/19/2025, 8:58:31 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        seen = set()

        def dfs(i):
            seen.add(i)
            for j in range(0, len(isConnected)):
                if isConnected[i][j]:
                    if j not in seen:
                        dfs(j)
        
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                ans += 1

        return ans
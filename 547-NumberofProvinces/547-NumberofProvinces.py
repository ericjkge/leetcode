# Last updated: 8/4/2025, 11:26:05 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        counter = 0
        
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)
        
        for i in range(len(isConnected)):
            if i not in seen:
                counter += 1
                seen.add(i)
                dfs(i)
        
        return counter
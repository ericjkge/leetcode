# Last updated: 7/9/2025, 12:47:19 PM
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = set()
        ans = 0
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((a, b))
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in connected or (j, i) in connected:
                    rank -= 1
                ans = max(ans, rank)
        
        return ans 

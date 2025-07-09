# Last updated: 7/9/2025, 12:34:11 PM
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    rank -= 1
                ans = max(ans, rank)

        print(graph)
        return ans
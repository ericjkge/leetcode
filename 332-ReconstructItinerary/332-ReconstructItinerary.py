# Last updated: 4/25/2026, 1:45:43 PM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        graph = defaultdict(list)
4
5        for src, dst in tickets:
6            heapq.heappush(graph[src], dst)
7        
8        res = []
9
10        def dfs(node):
11            while graph[node]:
12                dfs(heapq.heappop(graph[node]))
13            res.append(node)
14        
15        dfs("JFK")
16        return res[::-1]
17
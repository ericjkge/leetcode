# Last updated: 5/19/2026, 9:42:46 AM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        graph = defaultdict(list)
4
5        for src, dst in tickets:
6            heapq.heappush(graph[src], dst)
7        
8        order = []
9        def dfs(node):
10            while graph[node]:
11                dfs(heapq.heappop(graph[node]))
12            order.append(node)
13
14        dfs("JFK")
15        return order[::-1]
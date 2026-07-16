# Last updated: 7/15/2026, 11:35:10 PM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3        neighbors = defaultdict(list)
4        
5        for u, v in tickets:
6            heapq.heappush(neighbors[u], v)
7
8        order = []
9        def dfs(node):
10            while neighbors[node]:
11                dfs(heapq.heappop(neighbors[node]))
12            order.append(node)
13
14        dfs("JFK")
15        return order[::-1]
16        
17            
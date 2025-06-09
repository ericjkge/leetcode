# Last updated: 6/8/2025, 9:16:18 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        heap = [(0, src, k + 1)] # dist, node, remaining stops
        visited = {}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > 0:
                for nei, weight in graph[node]:
                    state = (nei, stops - 1)
                    if state not in visited or (cost + weight) < visited[state]:
                        visited[state] = cost + weight
                        heapq.heappush(heap, (cost + weight, nei, stops - 1))
        
        return -1
        
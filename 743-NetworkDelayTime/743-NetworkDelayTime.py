# Last updated: 8/8/2025, 9:57:35 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for start, end, weight in times:
            if start not in graph:
                graph[start] = []
            graph[start].append((end, weight))
        
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heap = [(0, k)]
        
        while heap:
            curr, node = heapq.heappop(heap)
            if curr > distances[node]:
                continue
        		
            for nei, weight in graph.get(node, []):
        	    dist = curr + weight
        	    if dist < distances[nei]:
        	        distances[nei] = dist
        	        heapq.heappush(heap, (dist, nei))
        
        max_dist = max(distances[1:])
        return max_dist if max_dist != float("inf") else -1
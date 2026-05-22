# Last updated: 5/22/2026, 1:14:05 PM
1class Solution:
2    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
3        intervals.sort()
4        sorted_queries = sorted((q, i) for i, q in enumerate(queries)) 
5        res = [-1] * len(queries)
6        heap = []
7        i = 0
8
9        for query, index in sorted_queries:
10            while i < len(intervals) and intervals[i][0] <= query:
11                start, end = intervals[i]
12                heapq.heappush(heap, (end - start + 1, end))
13                i += 1
14
15            while heap and heap[0][1] < query:
16                heapq.heappop(heap)
17            
18            if heap:
19                res[index] = heap[0][0]
20        
21        return res
22
23
24
# Last updated: 8/8/2025, 7:57:06 PM
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        ans = float("inf")
        max_heap = []
        total_q = 0
        
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_q += q
            
            if len(max_heap) > k:
                total_q += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                ans = min(ans, total_q * ratio)
            
        return ans
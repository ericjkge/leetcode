# Last updated: 9/25/2025, 10:00:19 AM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        factors = [2, 3, 5]
        seen = set()

        while len(seen) < n:
            smallest = heapq.heappop(heap)
            if smallest not in seen:
                seen.add(smallest)
                for factor in factors:
                    heapq.heappush(heap, factor * smallest)
                    
        return max(seen)

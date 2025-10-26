# Last updated: 10/26/2025, 10:23:57 AM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = set([1])
        heap = [1]

        for _ in range(n):
            ans = heapq.heappop(heap)
            for factor in factors:
                if ans * factor not in seen:
                    seen.add(ans * factor)
                    heapq.heappush(heap, ans * factor)
        
        return ans
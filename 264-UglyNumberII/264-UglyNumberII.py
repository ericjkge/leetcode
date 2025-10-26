# Last updated: 10/26/2025, 12:34:50 AM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        factors = [2, 3, 5]
        seen = set()

        for i in range(n):
            ans = heapq.heappop(heap)
            for factor in factors:
                if ans * factor not in seen:
                    seen.add(ans * factor)
                    heapq.heappush(heap, ans * factor)

        return ans
# Last updated: 9/25/2025, 10:02:16 AM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set()
        factors = [2, 3, 5]

        for _ in range(n):
            ans = heapq.heappop(heap)
            for factor in factors:
                if ans * factor not in seen:
                    seen.add(ans * factor)
                    heapq.heappush(heap, ans * factor)

        return ans

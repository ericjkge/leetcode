# Last updated: 8/29/2025, 11:44:56 PM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set([1])
        factors = [2, 3, 5]

        for _ in range(n):
            ans = heapq.heappop(heap)
            for f in factors:
                if f * ans not in seen:
                    seen.add(f * ans)
                    heapq.heappush(heap, f * ans)    

        return ans

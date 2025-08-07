# Last updated: 8/7/2025, 11:30:48 PM
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        factors = [2, 3, 5]
        
        for _ in range(n):
            ans = heapq.heappop(heap)
            for f in factors:
                if ans * f not in seen:
                    seen.add(ans * f)
                    heapq.heappush(heap, ans * f)
            
        return ans
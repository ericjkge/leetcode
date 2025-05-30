# Last updated: 5/30/2025, 12:07:36 PM
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapq.heapify(weight)
        total = ans = 0
        while weight and total + weight[0] <= 5000:
            total += heapq.heappop(weight)
            ans += 1
            
        return ans
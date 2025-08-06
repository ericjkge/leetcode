# Last updated: 8/6/2025, 11:02:57 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        for num, freq in Counter(nums).items():
            heapq.heappush(heap, (-freq, num))
        
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
# Last updated: 5/3/2026, 11:02:40 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        counts = [(-val, key) for key, val in Counter(nums).items()]
4        heapq.heapify(counts)
5
6        ans = []
7        for _ in range(k):
8            val, key = heapq.heappop(counts)
9            ans.append(key)
10        
11        return ans
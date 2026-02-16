# Last updated: 2/16/2026, 11:28:27 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        counter = Counter(nums)
4        freqs = [(-val, key) for key, val in counter.items()]
5        heapq.heapify(freqs)
6
7        ans = []
8        for _ in range(k):
9            _, key = heapq.heappop(freqs)
10            ans.append(key)
11
12        return ans
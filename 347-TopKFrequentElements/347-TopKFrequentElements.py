# Last updated: 9/1/2026, 10:14:56 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freqs = Counter(nums)
4        heap = []
5
6        for num, freq in freqs.items():
7            heapq.heappush(heap, (-freq, num))
8
9        res = []
10        for _ in range(k):
11            _, num = heapq.heappop(heap)
12            res.append(num)
13
14        return res
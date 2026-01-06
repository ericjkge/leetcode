# Last updated: 1/6/2026, 10:12:37 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freqs = Counter(nums)
4        heap = [(-freq, num) for num, freq in freqs.items()]
5        heapq.heapify(heap)
6        ans = []
7
8        for _ in range(k):
9            freq, num = heapq.heappop(heap)
10            ans.append(num)
11        
12        return ans
13
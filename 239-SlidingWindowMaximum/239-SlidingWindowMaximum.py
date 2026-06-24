# Last updated: 6/23/2026, 8:40:57 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        res = []
4        heap = [(-num, i) for i, num in enumerate(nums[:k])]
5        heapq.heapify(heap)
6
7        for i in range(k, len(nums)):
8            while heap and heap[0][1] <= i - k - 1:
9                heapq.heappop(heap)
10
11            res.append(-heap[0][0])
12            heapq.heappush(heap, (-nums[i], i))
13    
14        while heap and heap[0][1] <= len(nums) - 1 - k:
15            heapq.heappop(heap)
16
17        res.append(-heap[0][0])
18        return res
19
# Last updated: 7/15/2026, 12:01:29 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        window = []
4        ans = [0] * (len(nums) - k + 1)
5
6        for i, num in enumerate(nums):
7            if i < k - 1:
8                heapq.heappush(window, (-num, i))
9                continue
10
11            heapq.heappush(window, (-num, i))
12            while window and window[0][1] <= i - k:
13                heapq.heappop(window)
14            
15            ans[i - k + 1] = -window[0][0]
16        
17        return ans
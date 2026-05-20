# Last updated: 5/20/2026, 9:50:53 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        window = deque()
4        mx = []
5
6        for i in range(len(nums)):
7            if window and window[0] <= i - k:
8                window.popleft()
9
10            while window and nums[i] >= nums[window[-1]]:
11                window.pop()
12            
13            window.append(i)
14
15            if i + 1 < k:
16                continue
17
18            mx.append(nums[window[0]])
19        
20        return mx
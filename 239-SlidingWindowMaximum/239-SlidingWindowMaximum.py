# Last updated: 2/21/2026, 10:39:52 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        dq = deque()
4        ans = []
5
6        for i, num in enumerate(nums):
7            if dq and dq[0] == i - k:
8                dq.popleft()
9
10            while dq and nums[dq[-1]] <= num:
11                dq.pop()
12            
13            dq.append(i)
14
15            if i >= k - 1:
16                ans.append(nums[dq[0]])
17        
18        return ans
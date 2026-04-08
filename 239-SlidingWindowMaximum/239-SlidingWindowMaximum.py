# Last updated: 4/8/2026, 5:14:02 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        ans = []
4        dq = deque()
5
6        for i, num in enumerate(nums):
7            while dq and nums[dq[-1]] < num:
8                dq.pop()
9            dq.append(i)
10
11            if i >= k - 1:
12                # print(dq)
13                if dq[0] == i - k:
14                    dq.popleft()
15                ans.append(nums[dq[0]])
16
17        return ans
# Last updated: 11/1/2026, 12:37:02 PM
1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3        left = 0
4        window = 0
5        ans = -float("inf")
6
7        for right in range(len(nums)):
8            window += nums[right]
9
10            if right < k - 1:
11                continue
12            else:
13                ans = max(ans, window)
14                window -= nums[left]
15                left += 1
16
17        return ans / k
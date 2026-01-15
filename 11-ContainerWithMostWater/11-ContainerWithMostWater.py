# Last updated: 1/15/2026, 10:19:28 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        amount = 0
5
6        while left < right:
7            amount = max(amount, min(height[left], height[right]) * (right - left))
8            if height[left] < height[right]:
9                left += 1
10            else:
11                right -= 1
12
13        return amount
# Last updated: 6/9/2026, 8:17:07 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        res = 0
4        left, right = 0, len(height) - 1
5
6        while left < right:
7            res = max(res, (right - left) * min(height[left], height[right]))
8            if height[left] < height[right]:
9                left += 1
10            else:
11                right -= 1
12        
13        return res
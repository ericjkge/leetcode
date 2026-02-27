# Last updated: 2/27/2026, 8:49:27 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        area = 0
5
6        while left < right:
7            w, h = right - left, min(height[left], height[right])
8            area = max(area, w * h)
9            if height[left] < height[right]:
10                left += 1
11            else:
12                right -= 1
13        
14        return area
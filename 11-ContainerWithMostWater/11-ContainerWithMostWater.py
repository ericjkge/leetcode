# Last updated: 11/1/2026, 11:28:40 AM
1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        left, right = 0, len(height) - 1
4        volume = 0
5
6        while left < right:
7            if height[left] < height[right]:
8                volume = max(volume, (right - left) * height[left])
9                left += 1
10            else:
11                volume = max(volume, (right - left) * height[right])
12                right -= 1
13        
14        return volume
# Last updated: 7/8/2026, 1:01:29 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        lheight, rheight = height[left], height[right]
5        total = 0
6
7        while left < right:
8            if lheight <= rheight:
9                left += 1
10                lheight = max(lheight, height[left])
11                total += lheight - height[left]
12            else:
13                right -= 1
14                rheight = max(rheight, height[right])
15                total += rheight - height[right]
16
17        return total
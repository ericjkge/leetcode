# Last updated: 7/17/2026, 8:22:05 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        mleft, mright = height[left], height[right]
5        mx = 0
6
7        while left < right:
8            mx = max(mx, (right - left) * min(mleft, mright))
9            if mleft < mright:
10                left += 1
11                mleft = max(mleft, height[left])
12            else:
13                right -= 1
14                mright = max(mright, height[right])
15
16        return mx
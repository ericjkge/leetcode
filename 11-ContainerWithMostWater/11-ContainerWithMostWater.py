# Last updated: 1/15/2026, 10:17:59 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        mleft, mright = height[left], height[right]
5        amount = min(mleft, mright) * (right - left)
6
7        while left < right:
8            if height[left] < height[right]:
9                left += 1
10                mleft = max(height[left], mleft)
11            else:
12                right -= 1
13                mright = max(height[right], mright)
14            amount = max(amount, min(mleft, mright) * (right - left))
15
16        return amount
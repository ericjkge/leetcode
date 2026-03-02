# Last updated: 3/2/2026, 9:34:22 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        mleft, mright = height[left], height[right]
5        total = 0
6
7        while left < right:
8            if mleft <= mright:
9                left += 1
10                mleft = max(mleft, height[left])
11                total += mleft - height[left]
12            else:
13                right -= 1
14                mright = max(mright, height[right])
15                total += mright - height[right]
16
17        return total
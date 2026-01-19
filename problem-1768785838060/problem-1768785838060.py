# Last updated: 1/19/2026, 9:23:58 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        mleft, mright = height[left], height[right]
5        water = 0
6
7        while left < right:
8            if mleft <= mright:
9                left += 1
10                mleft = max(mleft, height[left])
11                water += mleft - height[left]
12            else:
13                right -= 1
14                mright = max(mright, height[right])
15                water += mright - height[right]
16
17        return water
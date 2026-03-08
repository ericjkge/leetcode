# Last updated: 3/8/2026, 9:58:22 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        ans = 0
5
6        for index, height in enumerate(heights):
7            start = index
8            while stack and stack[-1][1] > height:
9                i, h = stack.pop()
10                start = i
11                area = h * (index - i)
12                ans = max(ans, area)
13            stack.append((start, height))
14
15        while stack:
16            i, h = stack.pop()
17            area = h * (len(heights) - i)
18            ans = max(ans, area)
19
20        return ans
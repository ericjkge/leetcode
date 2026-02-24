# Last updated: 2/24/2026, 9:36:02 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        area = 0
5
6        for i, h in enumerate(heights):
7            start = i
8            while stack and h < stack[-1][1]:
9                index, height = stack.pop()
10                area = max(area, (i - index) * height)
11                start = index
12            stack.append((start, h))
13        
14        while stack:
15            index, height = stack.pop()
16            area = max(area, (len(heights) - index) * height)
17        
18        return area
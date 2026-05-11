# Last updated: 5/11/2026, 10:42:03 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        largest = 0
5
6        for index, height in enumerate(heights):
7            start = index
8            while stack and stack[-1][1] > height:
9                i, h = stack.pop()
10                largest = max(largest, (index - i) * h)
11                start = i
12            stack.append((start, height))
13
14        while stack:
15            i, h = stack.pop()
16            largest = max(largest, (len(heights) - i) * h)
17
18        return largest
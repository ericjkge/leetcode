# Last updated: 5/11/2026, 10:40:29 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        largest = 0
5
6        for i, height in enumerate(heights):
7            pi = None
8            while stack and stack[-1][1] > height:
9                pi, pheight = stack.pop()
10                largest = max(largest, (i - pi) * pheight)
11            if pi is not None:
12                stack.append((pi, height))
13            stack.append((i, height))
14
15        while stack:
16            pi, pheight = stack.pop()
17            largest = max(largest, (len(heights) - pi) * pheight)
18
19        return largest
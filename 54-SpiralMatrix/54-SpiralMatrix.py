# Last updated: 3/5/2026, 9:30:05 AM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        top, bottom = 0, len(matrix)
4        left, right = 0, len(matrix[0])
5        res = []
6
7        while top < bottom and left < right:
8            for col in range(left, right):
9                res.append(matrix[top][col])
10            top += 1
11
12            for row in range(top, bottom):
13                res.append(matrix[row][right - 1])
14            right -= 1
15
16            if top >= bottom or left >= right:
17                break
18
19            for col in range(right - 1, left - 1, -1):
20                res.append(matrix[bottom - 1][col])
21            bottom -= 1
22
23            for row in range(bottom - 1, top - 1, -1):
24                res.append(matrix[row][left])
25            left += 1
26
27        return res
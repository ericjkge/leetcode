# Last updated: 1/24/2026, 10:18:54 AM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        elements = []
4        left, right = 0, len(matrix[0]) - 1
5        top, bottom = 0, len(matrix) - 1
6
7        while left <= right and top <= bottom:
8            for c in range(left, right + 1):
9                elements.append(matrix[top][c])
10            top += 1
11
12            for r in range(top, bottom + 1):
13                elements.append(matrix[r][right])
14            right -= 1
15
16            if not (left <= right and top <= bottom):
17                break
18
19            for c in range(right, left - 1, -1):
20                elements.append(matrix[bottom][c])
21            bottom -= 1
22            
23            for r in range(bottom, top - 1, -1):
24                elements.append(matrix[r][left])
25            left += 1
26
27        return elements
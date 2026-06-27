# Last updated: 6/27/2026, 12:00:07 PM
1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        res = [[0] * n for _ in range(n)]
4        left, right = 0, n - 1
5        top, bottom = 0, n - 1
6        i = 1
7
8        while left <= right and top <= bottom:
9            for col in range(left, right + 1):
10                res[top][col] = i
11                i += 1
12            top += 1
13            
14            for row in range(top, bottom + 1):
15                res[row][right] = i
16                i += 1
17            right -= 1
18
19            if left > right or top > bottom:
20                break
21
22            for col in range(right, left - 1, -1):
23                res[bottom][col] = i
24                i += 1
25            bottom -= 1
26            
27            for row in range(bottom, top - 1, -1):
28                res[row][left] = i
29                i += 1
30            left += 1
31                
32        return res
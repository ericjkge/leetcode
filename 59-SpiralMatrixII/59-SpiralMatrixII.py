# Last updated: 6/27/2026, 12:00:01 PM
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
11                print(res)
12                i += 1
13            top += 1
14            
15            for row in range(top, bottom + 1):
16                res[row][right] = i
17                print(res)
18                i += 1
19            right -= 1
20
21            if left > right or top > bottom:
22                break
23
24            for col in range(right, left - 1, -1):
25                res[bottom][col] = i
26                print(res)
27                i += 1
28            bottom -= 1
29            
30            for row in range(bottom, top - 1, -1):
31                res[row][left] = i
32                print(res)
33                i += 1
34            left += 1
35                
36        return res
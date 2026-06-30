# Last updated: 6/29/2026, 8:15:28 PM
1class Solution:
2    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
3        i, j = 0, 0
4        res = []
5        rows, cols = len(mat), len(mat[0])
6        up = True
7
8        for _ in range(rows * cols):
9            res.append(mat[i][j])
10            if up:
11                if j == cols - 1:
12                    i += 1
13                    up = False
14                elif i == 0:
15                    j += 1
16                    up = False
17                else:
18                    i -= 1
19                    j += 1
20            else:
21                if i == rows - 1:
22                    j += 1
23                    up = True
24                elif j == 0:
25                    i += 1
26                    up = True
27                else:
28                    i += 1
29                    j -= 1
30        
31        return res
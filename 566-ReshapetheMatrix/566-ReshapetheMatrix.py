# Last updated: 6/29/2026, 8:24:02 PM
1class Solution:
2    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
3        m, n = len(mat), len(mat[0])
4
5        if r * c != m * n:
6            return mat
7        
8        new = []
9        row = []
10        for i in range(m):
11            for j in range(n):
12                row.append(mat[i][j])
13                
14                if len(row) == c:
15                    new.append(row)
16                    row = []
17        
18        return new
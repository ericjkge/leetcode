# Last updated: 6/29/2026, 8:07:04 PM
1class Solution:
2    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
3        rows, cols = len(mat), len(mat[0])
4        starts = [(i, 0) for i in range(rows)] + [(rows - 1, i) for i in range(1, cols)]
5        diags = []
6
7        for r, c in starts:
8            i, j = r, c
9            diag = []
10            while i >= 0 and j < cols:
11                diag.append(mat[i][j])
12                i -= 1
13                j += 1
14            diags.append(diag)
15
16        for i in range(len(diags)):
17            if i % 2 == 0:
18                continue
19            diags[i].reverse()
20
21        return [num for diag in diags for num in diag]
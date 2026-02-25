# Last updated: 2/25/2026, 3:55:43 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        def create_board(state):
4            res = []
5            for row in state:
6                res.append("".join(row))
7            return res
8    
9        def backtrack(row, cols, diags, anti_diags, state):
10            if row == n:
11                ans.append(create_board(state))
12                return
13            
14            for col in range(n):
15                diag = row - col
16                anti_diag = row + col
17
18                if col in cols or diag in diags or anti_diag in anti_diags:
19                    continue
20
21                cols.add(col)
22                diags.add(diag)
23                anti_diags.add(anti_diag)
24                state[row][col] = "Q"
25
26                backtrack(row + 1, cols, diags, anti_diags, state)
27
28                cols.remove(col)
29                diags.remove(diag)
30                anti_diags.remove(anti_diag)
31                state[row][col] = "."
32            
33        ans = []
34        empty = [["."] * n for _ in range(n)]
35        backtrack(0, set(), set(), set(), empty)
36        return ans
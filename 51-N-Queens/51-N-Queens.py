# Last updated: 3/14/2026, 9:02:20 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        def convert_board(state):
4            res = []
5            for row in state:
6                res.append("".join(row))
7            return res
8
9        def backtrack(row, cols, diags, anti_diags, state):
10            if row == n:
11                string = convert_board(state)
12                ans.append(string)
13                return
14            
15            for col in range(n):
16                diag = row + col
17                anti_diag = row - col
18                if col not in cols and diag not in diags and anti_diag not in anti_diags:
19                    cols.add(col)
20                    diags.add(diag)
21                    anti_diags.add(anti_diag)
22                    state[row][col] = "Q"
23                    backtrack(row + 1, cols, diags, anti_diags, state)
24                    cols.remove(col)
25                    diags.remove(diag)
26                    anti_diags.remove(anti_diag)
27                    state[row][col] = "."
28
29        ans = []
30        board = [["."] * n for _ in range(n)]
31        backtrack(0, set(), set(), set(), board)
32        return ans
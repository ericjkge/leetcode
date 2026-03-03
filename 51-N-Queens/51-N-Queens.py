# Last updated: 3/3/2026, 9:25:12 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        def board_to_str(board):
4            res = []
5            for row in board:
6                res.append("".join(row))
7            return res
8
9        solutions = []
10        def backtrack(row, cols, diags, anti_diags, state):
11            if row == n:
12                solutions.append(board_to_str(state))
13                return
14            
15            for col in range(n):
16                diag = row - col
17                anti_diag = row + col
18                if col not in cols and diag not in diags and anti_diag not in anti_diags:
19                    state[row][col] = "Q"
20                    cols.add(col)
21                    diags.add(diag)
22                    anti_diags.add(anti_diag)
23                    backtrack(row + 1, cols, diags, anti_diags, state)
24                    state[row][col] = "."
25                    cols.remove(col)
26                    diags.remove(diag)
27                    anti_diags.remove(anti_diag)
28        
29        empty = [["."] * n for _ in range(n)]
30        backtrack(0, set(), set(), set(), empty)
31        return solutions
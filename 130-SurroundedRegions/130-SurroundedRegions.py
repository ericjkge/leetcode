# Last updated: 1/30/2026, 8:33:55 AM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
7        rows, cols = len(board), len(board[0])
8
9        def dfs(r, c):
10            for dr, dc in directions:
11                nr, nc = r + dr, c + dc
12                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
13                    board[nr][nc] = "T"
14                    dfs(nr, nc)
15
16        for c in range(cols):
17            if board[0][c] == "O":
18                board[0][c] = "T"
19                dfs(0, c)
20            
21            if board[rows - 1][c] == "O":
22                board[rows - 1][c] = "T"
23                dfs(rows - 1, c)
24        
25        for r in range(rows):
26            if board[r][0] == "O":
27                board[r][0] = "T"
28                dfs(r, 0)
29
30            if board[r][cols - 1] == "O":
31                board[r][cols - 1] = "T"
32                dfs(r, cols - 1)
33        
34        for r in range(rows):
35            for c in range(cols):
36                if board[r][c] == "O":
37                    board[r][c] = "X"
38                elif board[r][c] == "T":
39                    board[r][c] = "O"
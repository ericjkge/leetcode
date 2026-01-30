# Last updated: 1/30/2026, 8:34:37 AM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
7        rows, cols = len(board), len(board[0])
8
9        def dfs(r, c):
10            board[r][c] = "T"
11            for dr, dc in directions:
12                nr, nc = r + dr, c + dc
13                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
14                    dfs(nr, nc)
15
16        for c in range(cols):
17            if board[0][c] == "O":
18                dfs(0, c)
19            
20            if board[rows - 1][c] == "O":
21                dfs(rows - 1, c)
22        
23        for r in range(rows):
24            if board[r][0] == "O":
25                dfs(r, 0)
26
27            if board[r][cols - 1] == "O":
28                dfs(r, cols - 1)
29        
30        for r in range(rows):
31            for c in range(cols):
32                if board[r][c] == "O":
33                    board[r][c] = "X"
34                elif board[r][c] == "T":
35                    board[r][c] = "O"
# Last updated: 12/17/2025, 8:11:43 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
7        rows, cols = len(board), len(board[0])
8
9        def dfs(r, c):
10            board[r][c] = "S"
11            for dr, dc in directions:
12                nr, nc = r + dr, c + dc
13                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
14                    dfs(nr, nc)
15
16        for col in range(cols):
17            if board[0][col] == "O":
18                dfs(0, col)
19            if board[rows - 1][col] == "O":
20                dfs(rows - 1, col)
21        
22        for row in range(rows):
23            if board[row][0] == "O":
24                dfs(row, 0)
25            if board[row][cols - 1] == "O":
26                dfs(row, cols - 1)
27        
28        for row in range(rows):
29            for col in range(cols):
30                if board[row][col] == "S":
31                    board[row][col] = "O"
32                elif board[row][col] == "O":
33                    board[row][col] = "X"
34        
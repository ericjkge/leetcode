# Last updated: 8/8/2026, 5:05:56 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows, cols = len(board), len(board[0])
7        queue = deque()
8        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
9
10        for r in range(rows):
11            if board[r][0] == "O":
12                board[r][0] = "E"
13                queue.append((r, 0))
14            if board[r][cols - 1] == "O":
15                board[r][cols - 1] = "E"
16                queue.append((r, cols - 1))
17        
18        for c in range(1, cols - 1):
19            if board[0][c] == "O":
20                board[0][c] = "E"
21                queue.append((0, c))
22            if board[rows - 1][c] == "O":
23                board[rows - 1][c] = "E"
24                queue.append((rows - 1, c))
25
26        while queue:
27            r, c = queue.popleft()
28            for dr, dc in directions:
29                nr, nc = r + dr, c + dc
30                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
31                    board[nr][nc] = "E"
32                    queue.append((nr, nc))
33        
34        for r in range(rows):
35            for c in range(cols):
36                if board[r][c] == "E":
37                    board[r][c] = "O"
38                elif board[r][c] == "O":
39                    board[r][c] = "X"
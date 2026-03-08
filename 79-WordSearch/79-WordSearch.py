# Last updated: 3/8/2026, 9:15:44 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m, n = len(board), len(board[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def backtrack(r, c, index):
7            if index == len(word):
8                return True
9            
10            for dr, dc in directions:
11                nr, nc = r + dr, c + dc
12                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[index]:
13                    old = board[nr][nc]
14                    board[nr][nc] = "#"
15                    if backtrack(nr, nc, index + 1):
16                        return True
17                    board[nr][nc] = old
18
19            return False
20
21        for r in range(m):
22            for c in range(n):
23                if board[r][c] == word[0]:
24                    old = board[r][c]
25                    board[r][c] = "#"
26                    if backtrack(r, c, 1):
27                        return True
28                    board[r][c] = old
29
30        return False
31
32
33                    
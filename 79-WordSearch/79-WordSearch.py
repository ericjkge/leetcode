# Last updated: 1/27/2026, 9:23:37 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows, cols = len(board), len(board[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def backtrack(r, c, index):
7            if index == len(word):
8                return True
9    
10            original = board[r][c]
11            board[r][c] = "*"
12
13            for dr, dc in directions:
14                nr, nc = r + dr, c + dc
15                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[index]:
16                    if backtrack(nr, nc, index + 1):
17                        return True
18
19            board[r][c] = original
20            return False
21
22        for r in range(rows):
23            for c in range(cols):
24                if board[r][c] == word[0] and backtrack(r, c, 1):
25                    return True
26        return False
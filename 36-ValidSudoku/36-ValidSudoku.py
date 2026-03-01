# Last updated: 3/1/2026, 1:53:27 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows, cols = len(board), len(board[0])
4
5        for r in range(rows):
6            seen = set()
7            for c in range(cols):
8                if board[r][c] == ".":
9                    continue
10                if board[r][c] in seen:
11                    return False
12                seen.add(board[r][c])
13
14        for c in range(cols):
15            seen = set()
16            for r in range(rows):
17                if board[r][c] == ".":
18                    continue
19                if board[r][c] in seen:
20                    return False
21                seen.add(board[r][c])
22
23        for r in range(0, rows, 3):
24            for c in range(0, cols, 3):
25                seen = set()
26                for i in range(3):
27                    for j in range(3):
28                        if board[r + i][c + j] == ".":
29                            continue
30                        if board[r + i][c + j] in seen:
31                            return False
32                        seen.add(board[r + i][c + j])
33        
34        return True
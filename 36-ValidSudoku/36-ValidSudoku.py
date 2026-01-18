# Last updated: 1/18/2026, 10:35:41 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3
4        for row in range(9):
5            seen = set()
6            for col in range(9):
7                if board[row][col].isalnum() and board[row][col] in seen:
8                    return False
9                seen.add(board[row][col])
10    
11        for col in range(9):
12            seen = set()
13            for row in range(9):
14                if board[row][col].isalnum() and board[row][col] in seen:
15                    return False
16                seen.add(board[row][col])
17
18        for row in range(0, 9, 3):
19            for col in range(0, 9, 3):
20                seen = set()
21                for r in range(row, row + 3):
22                    for c in range(col, col + 3):
23                        if board[r][c].isalnum() and board[r][c] in seen:
24                            return False
25                        seen.add(board[r][c])
26                        
27        return True
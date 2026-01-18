# Last updated: 1/18/2026, 10:08:43 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        for row in board:
4            seen = set()
5            for num in row:
6                if num.isalnum() and num in seen:
7                    return False
8                seen.add(num)
9
10        for i in range(9):
11            seen = set()
12            for j in range(9):
13                if board[j][i].isalnum() and board[j][i] in seen:
14                    return False
15                seen.add(board[j][i])
16
17        for i in range(0, 9, 3):
18            for j in range(0, 9, 3):
19                seen = set()
20                for k in range(i, i + 3):
21                    for l in range(j, j + 3):
22                        if board[k][l].isalnum() and board[k][l] in seen:
23                            return False
24                        seen.add(board[k][l])
25
26        return True
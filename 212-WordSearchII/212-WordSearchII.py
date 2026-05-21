# Last updated: 5/21/2026, 10:56:19 AM
1class Solution:
2    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
3        root = {}
4        for word in words:
5            curr = root
6            for c in word:
7                if c not in curr:
8                    curr[c] = {}
9                curr = curr[c]
10            curr["$"] = word
11        
12        rows, cols = len(board), len(board[0])
13        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
14        res = []
15
16        def backtrack(r, c, parent):
17            if "$" in parent:
18                res.append(parent["$"])
19            
20            for dr, dc in directions:
21                nr, nc = r + dr, c + dc
22                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in parent:
23                    original = board[nr][nc]
24                    board[nr][nc] = "*"
25                    backtrack(nr, nc, parent[original])
26                    board[nr][nc] = original
27        
28        for r in range(rows):
29            for c in range(cols):
30                letter = board[r][c]
31                if letter in root:
32                    board[r][c] = "*"
33                    backtrack(r, c, root[letter])
34                    board[r][c] = letter
35
36        return list(set(res))
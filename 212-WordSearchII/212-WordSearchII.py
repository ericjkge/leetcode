# Last updated: 5/21/2026, 10:43:54 AM
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
12        print(root)
13        rows, cols = len(board), len(board[0])
14        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
15        res = []
16
17        def backtrack(r, c, parent):
18            if "$" in parent:
19                res.append(parent["$"])
20            
21            for dr, dc in directions:
22                nr, nc = r + dr, c + dc
23                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in parent:
24                    original = board[nr][nc]
25                    board[nr][nc] = "*"
26                    backtrack(nr, nc, parent[original])
27                    board[nr][nc] = original
28        
29        for r in range(rows):
30            for c in range(cols):
31                letter = board[r][c]
32                if letter in root:
33                    board[r][c] = "*"
34                    backtrack(r, c, root[letter])
35                    board[r][c] = letter
36                    
37        return list(set(res))
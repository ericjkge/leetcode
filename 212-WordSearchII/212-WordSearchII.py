# Last updated: 2/21/2026, 10:05:45 AM
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
14        ans = []
15
16        def backtrack(r, c, parent):
17            char = board[r][c]
18            if char not in parent:
19                return
20            curr = parent[char]
21
22            word = curr.pop("$", None)
23            if word:
24                ans.append(word)
25            board[r][c] = "#"
26
27            for dr, dc in directions:
28                nr, nc = r + dr, c + dc
29                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
30                    backtrack(nr, nc, curr)        
31
32            board[r][c] = char
33            if not curr:
34                parent.pop(char)
35
36        for r in range(rows):
37            for c in range(cols):
38                backtrack(r, c, root)
39        
40        return ans
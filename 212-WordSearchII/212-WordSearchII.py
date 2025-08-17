# Last updated: 8/17/2025, 7:41:45 PM
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["$"] = word
        
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []

        def backtrack(r, c, parent):
            char = board[r][c]
            if char not in parent:
                return False
            curr = parent[char]

            word = curr.pop("$", None)
            if word:
                ans.append(word)
            board[r][c] = "#"

            if curr:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                        backtrack(nr, nc, curr)
            board[r][c] = char
            if not curr:
                parent.pop(char)
                
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)
        return ans
# Last updated: 11/14/2025, 2:29:40 PM
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "X":
                    continue
                
                if r > 0 and board[r - 1][c] == "X":
                    continue
                
                if c > 0 and board[r][c - 1] == "X":
                    continue
                
                ans += 1
        
        return ans
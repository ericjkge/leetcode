# Last updated: 9/3/2025, 11:03:43 AM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, cols, diag, anti_diag, state):
            if row == n:
                ans.append(create_board(state))
                return
            
            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col
                if col in cols or curr_diag in diag or curr_anti_diag in anti_diag:
                    continue
                cols.add(col)
                diag.add(curr_diag)
                anti_diag.add(curr_anti_diag)
                state[row][col] = "Q"
                
                backtrack(row + 1, cols, diag, anti_diag, state)

                cols.remove(col)
                diag.remove(curr_diag)
                anti_diag.remove(curr_anti_diag)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
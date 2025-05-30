# Last updated: 5/30/2025, 12:07:42 PM
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        
        def intToPos(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2:
                col = n - 1 - col
            return [row, col]
        
        queue = deque()
        queue.append([1, 0])
        seen = set()
        
        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                row, col = intToPos(nextSquare)
                
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in seen:
                    seen.add(nextSquare)
                    queue.append([nextSquare, moves + 1])
        return -1
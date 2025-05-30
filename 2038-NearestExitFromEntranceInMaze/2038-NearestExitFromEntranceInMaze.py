# Last updated: 5/30/2025, 12:07:24 PM
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:    
        def isValid(position):
            return 0 <= position[0] < len(maze) and 0 <= position[1] < len(maze[0])
            
        def onBoundary(position):
            return position[0] == 0 or position[0] == len(maze) - 1 or position[1] == 0 or position[1] == len(maze[0]) - 1
        
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        queue = deque([entrance])
        seen = {tuple(entrance)}
        counter = 0
        
        while queue:
            level = len(queue)
            for _ in range(level):
                position = queue.popleft()
                if onBoundary(position) and position != entrance:
                    return counter
                
                for dx, dy in directions:
                    next_row = position[0] + dx
                    next_col = position[1] + dy
                    
                    if isValid([next_row, next_col]) and (next_row, next_col) not in seen and maze[next_row][next_col] != "+":
                        seen.add((next_row, next_col))
                        queue.append([next_row, next_col])
            counter += 1
            
        return -1
                        
            
        
# Last updated: 8/12/2025, 12:03:40 AM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def neighbors(number):
            options = []
            for i in range(4):
                d = int(number[i])
                for diff in (-1, 1):
                    nd = (d + diff) % 10
                    options.append(number[:i] + str(nd) + number[i + 1:])
            return options
        
        queue = deque(["0000"])
        seen = set("0000")
        moves = 0
        
        while queue:
            for _ in range(len(queue)):
                number = queue.popleft()
                if number == target:
                    return moves
                for neighbor in neighbors(number):
                    if neighbor not in seen and neighbor not in deadends:
                        seen.add(neighbor)
                        queue.append(neighbor)
            moves += 1
        
        return -1
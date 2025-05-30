# Last updated: 5/30/2025, 12:07:30 PM
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        length = len(arr)
        queue = deque([start])
        seen = {start}
        
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for next_index in [-arr[index], arr[index]]:
                if (index + next_index) not in seen and 0 <= (index + next_index) < length:
                    seen.add(index + next_index)
                    queue.append(index + next_index)
        
        return False
            
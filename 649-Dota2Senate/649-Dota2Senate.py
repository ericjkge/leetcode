# Last updated: 7/7/2025, 12:47:31 AM
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()

        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(len(senate) + 1 + r)
            else:
                d_queue.append(len(senate) + d)
    
        return "Radiant" if r_queue else "Dire"
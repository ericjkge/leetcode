# Last updated: 12/1/2025, 10:47:13 AM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        stones = [-stone for stone in stones]
4        heapq.heapify(stones)
5
6        if not stones:
7            return None
8
9        while len(stones) > 1:
10            s1, s2 = -heapq.heappop(stones), -heapq.heappop(stones)
11            
12            if s1 > s2:
13                heapq.heappush(stones, -(s1 - s2))
14        
15        return -stones[0] if stones else 0
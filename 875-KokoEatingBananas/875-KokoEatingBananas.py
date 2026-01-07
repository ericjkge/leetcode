# Last updated: 1/7/2026, 11:15:55 AM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        def canEat(speed):
4            time = 0
5            for pile in piles:
6                time += (pile + speed - 1) // speed
7            return time <= h
8
9        left, right = 1, max(piles)
10        while left + 1 < right:
11            mid = (left + right) // 2
12            if canEat(mid):
13                right = mid
14            else:
15                left = mid
16        
17        if canEat(left):
18            return left
19        return right
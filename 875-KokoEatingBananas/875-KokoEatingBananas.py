# Last updated: 11/13/2026, 1:42:13 AM
1class Solution:
2    def minEatingSpeed(self, piles: list[int], h: int) -> int:
3        def canEat(speed):
4            time = 0
5            for pile in piles:
6                if pile % speed == 0:
7                    time += pile // speed
8                else:
9                    time += pile // speed + 1
10            return time <= h
11        
12        left, right = 1, max(piles)
13        while left + 1 < right:
14            mid = (left + right) // 2
15            if canEat(mid):
16                right = mid
17            else:
18                left = mid
19        if canEat(left):
20            return left
21        return right
# Last updated: 7/8/2026, 10:35:04 AM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        def canEat(speed):
4            time = 0
5            for pile in piles:
6                if pile % speed:
7                    time += pile // speed + 1
8                else:
9                    time += pile // speed
10
11            return time <= h
12        
13        left, right = 1, max(piles)
14        while left + 1 < right:
15            mid = (left + right) // 2
16            if canEat(mid):
17                right = mid
18            else:
19                left = mid
20        
21        if canEat(left):
22            return left
23        return right
24
25                
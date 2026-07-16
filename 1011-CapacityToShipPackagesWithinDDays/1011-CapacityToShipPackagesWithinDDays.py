# Last updated: 7/15/2026, 8:02:53 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        def canShip(capacity):
4            count = 0
5            total = 0
6            for weight in weights:
7                if total + weight > capacity:
8                    total = 0
9                    count += 1
10                
11                total += weight
12            
13            count += 1
14            return count <= days
15                
16        left, right = max(weights), sum(weights)
17        while left + 1 < right:
18            mid = (left + right) // 2
19            if canShip(mid):
20                right = mid
21            else:
22                left = mid
23            
24        if canShip(left):
25            return left
26        return right
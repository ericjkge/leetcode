# Last updated: 7/15/2026, 8:02:50 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        def canShip(capacity):
4            count = 0
5            total = 0
6            for weight in weights:
7                if total + weight > capacity:
8                    print(total)
9                    total = 0
10                    count += 1
11                
12                total += weight
13            
14            count += 1
15            return count <= days
16                
17        left, right = max(weights), sum(weights)
18        while left + 1 < right:
19            mid = (left + right) // 2
20            if canShip(mid):
21                right = mid
22            else:
23                left = mid
24            
25        if canShip(left):
26            return left
27        return right
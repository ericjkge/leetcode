# Last updated: 1/9/2026, 10:16:55 AM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        flags = [False, False, False]
4        a, b, c = target
5
6        for x, y, z in triplets:
7            if x == a and y <= b and z <= c:
8                flags[0] = True
9            if x <= a and y == b and z <= c:
10                flags[1] = True
11            if x <= a and y <= b and z == c:
12                flags[2] = True
13        
14        return all(flags)
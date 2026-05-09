# Last updated: 5/8/2026, 9:13:16 PM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        a, b, c = target
4        flags = [False, False, False]
5
6        for x, y, z in triplets:
7            if x == a and y <= b and z <= c:
8                flags[0] = True
9            if y == b and x <= a and z <= c:
10                flags[1] = True
11            if z == c and x <= a and y <= b:
12                flags[2] = True
13
14        return all(flags)
15
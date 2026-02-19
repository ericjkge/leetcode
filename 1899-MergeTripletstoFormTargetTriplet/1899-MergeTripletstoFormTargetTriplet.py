# Last updated: 2/19/2026, 9:21:48 AM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        x, y, z = target
4        flags = [False, False, False]
5
6        for a, b, c in triplets:
7            if a == x and b <= y and c <= z:
8                flags[0] = True
9            if b == y and a <= x and c <= z:
10                flags[1] = True
11            if c == z and a <= x and b <= y:
12                flags[2] = True
13        
14        return all(flags)
15
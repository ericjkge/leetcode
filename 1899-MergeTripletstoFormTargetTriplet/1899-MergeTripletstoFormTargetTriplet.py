# Last updated: 2/19/2026, 9:19:40 AM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        x, y, z = target
4        flags = [False, False, False]
5
6        for a, b, c in triplets:
7            if a <= x and b <= y and c <= z:
8                flags[0] = flags[0] or (a == x)
9                flags[1] = flags[1] or (b == y)
10                flags[2] = flags[2] or (c == z)
11        
12        return True if all(flags) else False
13
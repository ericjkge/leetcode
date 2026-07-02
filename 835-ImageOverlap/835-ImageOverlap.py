# Last updated: 7/1/2026, 11:33:02 PM
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        ones1, ones2 = [], []
5        freqs = defaultdict(int)
6
7        for i in range(n):
8            for j in range(n):
9                if img1[i][j] == 1:
10                    ones1.append((i, j))
11                if img2[i][j] == 1:
12                    ones2.append((i, j))
13        
14        for x, y in ones1:
15            for r, c in ones2:
16                dx, dy = r - x, c - y
17                freqs[(dx, dy)] += 1
18        
19        if freqs:
20            return max(freqs.values())
21        return 0
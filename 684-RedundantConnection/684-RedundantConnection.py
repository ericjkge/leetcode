# Last updated: 4/4/2026, 10:02:03 AM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        class UnionFind:
4            def __init__(self, n):
5                self.roots = [i for i in range(n + 1)]
6                self.heights = [0] * (n + 1)
7            
8            def find(self, x):
9                if self.roots[x] != x:
10                    self.roots[x] = self.find(self.roots[x])
11                return self.roots[x]
12
13            def union(self, a, b):
14                x, y = self.find(a), self.find(b)
15                if self.roots[x] == self.roots[y]:
16                    return True
17                
18                if self.heights[x] < self.heights[y]:
19                    self.roots[x] = self.roots[y]
20                elif self.heights[x] > self.heights[y]:
21                    self.roots[y] = self.roots[x]
22                else:
23                    self.roots[y] = self.roots[x]
24                    self.heights[x] += 1
25                return False
26            
27        uf = UnionFind(len(edges))
28        
29        for a, b in edges:
30            if uf.union(a, b):
31                return [a, b]
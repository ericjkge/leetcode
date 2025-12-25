# Last updated: 12/25/2025, 8:08:57 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        class UnionFind:
4            def __init__(self, size):
5                self.root = [i for i in range(size)]
6                self.rank = [1] * size
7
8            def find(self, x):
9                if self.root[x] != x:
10                    self.root[x] = self.find(self.root[x])
11                return self.root[x]
12            
13            def union(self, x, y):
14                rootX = self.find(x)
15                rootY = self.find(y)
16                if rootX == rootY:
17                    return False
18                if self.rank[x] < self.rank[y]:
19                    self.root[rootX] = rootY
20                elif self.rank[x] > self.rank[y]:
21                    self.root[rootY] = rootX
22                else:
23                    self.root[rootY] = rootX
24                    self.rank[rootX] += 1
25                return True
26        
27        uf = UnionFind(len(edges))
28
29        for x, y in edges:
30            if not uf.union(x - 1, y - 1):
31                return [x, y]
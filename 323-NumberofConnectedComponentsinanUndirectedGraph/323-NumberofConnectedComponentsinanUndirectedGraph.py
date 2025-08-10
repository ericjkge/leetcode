# Last updated: 8/10/2025, 11:48:42 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
            
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra != rb:
                    if self.rank[ra] > self.rank[rb]:
                        self.root[rb] = ra
                    elif self.rank[ra] < self.rank[rb]:
                        self.root[ra] = rb
                    else:
                        self.root[rb] = ra
                        self.rank[ra] += 1
        
        uf = UnionFind(n)
        for start, end in edges:
            uf.union(start, end)
        root = set([uf.find(i) for i in range(n)])
        return len(root)
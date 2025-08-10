# Last updated: 8/11/2025, 1:27:58 AM
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False
                if ra != rb:
                    if self.rank[ra] > self.rank[rb]:
                        self.root[rb] = ra
                    elif self.rank[ra] < self.rank[rb]:
                        self.root[ra] = rb
                    else:
                        self.root[rb] = ra
                        self.rank[ra] += 1
                return True
        
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []
        
        for r, c in positions:
            if grid[r][c] == 1: # Already processed
                ans.append(count)
                continue
            grid[r][c] = 1
            count += 1
            index = r * n + c
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    if uf.union(index, nr * n + nc):
                        count -= 1
            ans.append(count)
        return ans
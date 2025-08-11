# Last updated: 8/11/2025, 4:16:27 PM
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        root = [i for i in range(n)]
        rank = [1] * n
        counter = n
        
        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]
        
        def union(a, b):
            nonlocal counter
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                root[ra] = rb
            elif rank[ra] > rank[rb]:
                root[rb] = ra
            else:
                root[ra] = rb
                rank[rb] += 1
            counter -= 1
        
        connections.sort(key = lambda x: x[2])
        
        total = 0
        for a, b, weight in connections:
            if find(a - 1) != find(b - 1):
                total += weight
                union(a - 1, b - 1)
                
        return total if counter == 1 else -1
# Last updated: 8/1/2025, 4:51:25 PM
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        seen = set((0, 0))
        
        for _ in range(k - 1):
            val, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix) and (i + 1, j) not in seen:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                seen.add((i + 1, j))
            if j + 1 < len(matrix[0]) and (i, j + 1) not in seen:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                seen.add((i, j + 1))
            
        return heapq.heappop(heap)[0]
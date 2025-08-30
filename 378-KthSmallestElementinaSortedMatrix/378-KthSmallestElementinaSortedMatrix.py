# Last updated: 8/30/2025, 7:53:43 AM
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        seen = set((0, 0))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if (i + 1, j) not in seen and i + 1 < n:
                seen.add((i + 1, j))
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if (i, j + 1) not in seen and j + 1 < n:
                seen.add((i, j + 1))
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))

        return heap[0][0]
# Last updated: 7/10/2025, 3:36:17 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = costs[:candidates]
        right_heap = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        left = candidates
        right = len(costs) - 1 - candidates

        ans = 0
        for _ in range(k):
            left_cost = left_heap[0] if left_heap else float("inf")
            right_cost = right_heap[0] if right_heap else float("inf")

            if left_cost <= right_cost:
                ans += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                ans += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return ans

# Last updated: 7/10/2025, 3:32:09 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        left = 0
        right = len(costs) - 1

        if candidates * 2 > len(costs):
            heap = [cost for cost in costs]
            heapq.heapify(heap)
            return sum(heapq.heappop(heap) for _ in range(k))

        for _ in range(candidates):
            left_heap.append(costs[left])
            right_heap.append(costs[right])
            left += 1
            right -= 1
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        ans = 0
        flag = True # flag for whether to continue adding to either heap
        for _ in range(k):
            if left > right:
                flag = False

            left_cost = left_heap[0] if left_heap else float("inf")
            right_cost = right_heap[0] if right_heap else float("inf")

            if left_cost <= right_cost:
                ans += heapq.heappop(left_heap)
                if flag:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                ans += heapq.heappop(right_heap)
                if flag:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return ans

# Last updated: 7/10/2025, 5:50:43 PM
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        maximum = -float("inf")

        for i, lst in enumerate(nums):
            val = lst[0]
            heapq.heappush(heap, (val, i, 0))
            maximum = max(maximum, val)
        
        ans = [-float("inf"), float("inf")]

        while True:
            min_val, list_index, position_index = heapq.heappop(heap)

            if maximum - min_val < ans[1] - ans[0]:
                ans = [min_val, maximum]
            
            if position_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][position_index + 1]
                heapq.heappush(heap, (next_val, list_index, position_index + 1))
                maximum = max(maximum, next_val)
            else:
                break

        return ans
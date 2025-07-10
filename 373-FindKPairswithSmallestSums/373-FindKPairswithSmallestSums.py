# Last updated: 7/10/2025, 4:16:32 PM
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        seen = set((0, 0))

        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))
        
        return ans

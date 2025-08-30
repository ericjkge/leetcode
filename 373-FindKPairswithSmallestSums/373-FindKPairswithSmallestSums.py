# Last updated: 8/30/2025, 7:29:31 AM
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k = min(k, len(nums1) * len(nums2))
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set([(0, 0)])
        ans = []

        for _ in range(k):
            _, p1, p2 = heapq.heappop(heap)
            ans.append((nums1[p1], nums2[p2]))
            if p1 + 1 < len(nums1) and (p1 + 1, p2) not in seen:
                seen.add((p1 + 1, p2))
                heapq.heappush(heap, (nums1[p1 + 1] + nums2[p2], p1 + 1, p2))
            if p2 + 1 < len(nums2) and (p1, p2 + 1) not in seen:
                seen.add((p1, p2 + 1))
                heapq.heappush(heap, (nums1[p1] + nums2[p2 + 1], p1, p2 + 1))
        
        return ans
# Last updated: 6/27/2026, 3:12:10 PM
1class Solution:
2    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
3        mapping = defaultdict(list)
4        ans = 0
5
6        for i in range(len(nums1)):
7            for j in range(len(nums2)):
8                mapping[nums1[i] + nums2[j]].append((i, j))
9        
10        for i in range(len(nums3)):
11            for j in range(len(nums4)):
12                total = nums3[i] + nums4[j]
13                ans += len(mapping[-total])
14
15        return ans
# Last updated: 7/4/2026, 4:08:35 PM
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        mapping = {}
4        ans = float("inf")
5
6        for i, num in enumerate(nums):
7            reverse = int(str(num)[::-1])
8            if num in mapping:
9                ans = min(ans, i - mapping[num])
10            mapping[reverse] = i
11
12        return ans if ans != float("inf") else -1
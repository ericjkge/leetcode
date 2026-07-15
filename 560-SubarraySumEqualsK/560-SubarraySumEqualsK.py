# Last updated: 7/14/2026, 11:29:30 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix = 0
4        mapping = {0:1}
5        count = 0
6
7        for i, num in enumerate(nums):
8            prefix += num
9            count += mapping.get(prefix - k, 0)
10            mapping[prefix] = mapping.get(prefix, 0) + 1
11
12
13        return count
14
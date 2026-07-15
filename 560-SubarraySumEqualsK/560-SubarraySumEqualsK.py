# Last updated: 7/14/2026, 11:29:12 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix = 0
4        mapping = {0:1}
5        count = 0
6
7        for i, num in enumerate(nums):
8            prefix += num
9            complement = prefix - k
10            count += mapping.get(complement, 0)
11            mapping[prefix] = mapping.get(prefix, 0) + 1
12
13        return count
14
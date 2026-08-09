# Last updated: 8/9/2026, 1:34:40 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        mapping = {0:1}
4        prefix = 0
5        total = 0
6
7        for num in nums:
8            prefix += num
9            complement = prefix - k
10            if complement in mapping:
11                total += mapping[complement]
12            mapping[prefix] = mapping.get(prefix, 0) + 1
13
14        return total
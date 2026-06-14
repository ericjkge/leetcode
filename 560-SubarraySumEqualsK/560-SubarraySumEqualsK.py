# Last updated: 6/14/2026, 10:32:20 AM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix = 0
4        seen = {0:1}
5        count = 0
6
7        for num in nums:
8            prefix += num
9            if prefix - k in seen:
10                count += seen[prefix - k]
11            seen[prefix] = seen.get(prefix, 0) + 1
12        
13        return count
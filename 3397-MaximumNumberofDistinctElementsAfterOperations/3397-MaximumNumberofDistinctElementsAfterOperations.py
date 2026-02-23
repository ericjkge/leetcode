# Last updated: 2/22/2026, 11:39:51 PM
1class Solution:
2    def maxDistinctElements(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        prev = float("-inf")
5        distinct = 0
6
7        for num in nums:
8            potential = max(prev + 1, num - k)
9
10            if potential <= num + k:
11                distinct += 1
12                prev = potential
13        
14        return distinct
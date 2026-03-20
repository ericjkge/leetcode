# Last updated: 3/20/2026, 4:20:43 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nset = set(nums)
4        longest = 0
5
6        for num in nset:
7            if num - 1 in nset:
8                continue
9            
10            streak = 1
11            while num + 1 in nset:
12                num += 1
13                streak += 1
14            
15            longest = max(longest, streak)
16
17        return longest
# Last updated: 6/4/2026, 9:30:39 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        longest = 0
5
6        for num in num_set:
7            count = 1
8            if num - 1 in num_set:
9                continue
10            
11            while num + 1 in num_set:
12                count += 1
13                num = num + 1
14
15            longest = max(longest, count)
16
17        return longest
18            
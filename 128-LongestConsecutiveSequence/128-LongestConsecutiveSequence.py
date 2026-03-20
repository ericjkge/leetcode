# Last updated: 3/20/2026, 4:19:09 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4        streak = 0
5        seen = set()
6
7        for num in nums_set:
8            if num not in seen:
9                counter = 1
10                while num + 1 in nums_set:
11                    seen.add(num)
12                    counter += 1
13                    num += 1
14                streak = max(streak, counter)
15            
16        return streak
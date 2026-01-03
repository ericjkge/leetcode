# Last updated: 1/4/2026, 12:40:53 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        seen = set(nums)
4
5        ans = 0
6        for num in seen:
7            streak = 1
8            if num - 1 not in seen:
9                while num + 1 in seen:
10                    num += 1
11                    streak += 1 
12            ans = max(ans, streak)
13            
14        return ans
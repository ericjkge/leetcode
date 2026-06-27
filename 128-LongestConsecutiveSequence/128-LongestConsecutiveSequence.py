# Last updated: 6/27/2026, 2:49:41 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4        ans = 0
5
6        for num in nums_set:
7            if num - 1 in nums_set:
8                continue
9            
10            count = 1
11            while num + 1 in nums_set:
12                num += 1
13                count += 1
14            
15            ans = max(ans, count)
16
17        return ans
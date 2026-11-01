# Last updated: 11/1/2026, 1:04:22 PM
1class Solution:
2    def pivotIndex(self, nums: list[int]) -> int:
3        total = sum(nums)
4        prefix = 0
5
6        for i, num in enumerate(nums):
7            if (total - num) / 2 == prefix:
8                return i
9            prefix += num
10        
11        return -1
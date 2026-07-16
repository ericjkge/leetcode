# Last updated: 7/15/2026, 11:48:43 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total = sum(nums)
4        prefix = 0
5
6        for i, num in enumerate(nums):
7            if prefix == total - prefix - num:
8                return i
9            prefix += num
10        
11        return -1
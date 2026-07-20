# Last updated: 7/19/2026, 9:11:58 PM
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
11
12        return -1
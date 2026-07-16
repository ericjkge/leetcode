# Last updated: 7/15/2026, 11:46:06 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        prefix = 0
4
5        for i, num in enumerate(nums):
6            if prefix == sum(nums[i + 1:]):
7                return i
8            
9            prefix += num
10
11        return -1
1214
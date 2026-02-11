# Last updated: 2/11/2026, 2:39:23 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4
5        for i in range(len(nums) + 1):
6            if i not in nums_set:
7                return i
8
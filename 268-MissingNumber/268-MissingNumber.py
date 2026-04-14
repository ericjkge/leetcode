# Last updated: 4/14/2026, 9:46:07 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        return int(n * (n + 1) / 2 - sum(nums))
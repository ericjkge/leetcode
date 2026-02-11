# Last updated: 2/11/2026, 2:41:00 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        expected = n * (n + 1) // 2
5        actual = sum(nums)
6        return expected - actual
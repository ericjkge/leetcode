# Last updated: 1/31/2026, 1:08:21 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        total = 0
4        for num in nums:
5            total ^= num
6        return total
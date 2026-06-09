# Last updated: 6/8/2026, 8:51:04 PM
1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        return (max(nums) - min(nums)) * k
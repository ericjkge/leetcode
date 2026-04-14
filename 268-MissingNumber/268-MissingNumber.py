# Last updated: 4/14/2026, 9:44:33 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4        for i in range(len(nums) + 1):
5            if i not in nums_set:
6                return i
7        
# Last updated: 7/17/2026, 8:13:06 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        p1 = p2 = 0
7
8        while p2 < len(nums):
9            if nums[p2] != 0:
10                nums[p1], nums[p2] = nums[p2], nums[p1]
11                p1 += 1
12            p2 += 1
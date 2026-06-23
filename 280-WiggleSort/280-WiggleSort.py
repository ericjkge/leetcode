# Last updated: 6/22/2026, 11:55:15 PM
1class Solution:
2    def wiggleSort(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        for i in range(len(nums) - 1):
7            if i % 2 == 0:
8                if nums[i] > nums[i + 1]:
9                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
10            else:
11                if nums[i] < nums[i + 1]:
12                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
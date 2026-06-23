# Last updated: 6/22/2026, 11:33:56 PM
1class Solution:
2    def wiggleSort(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        nums.sort()
7        res = nums[:]
8        half = (len(nums) + 1) // 2
9
10        nums[::2] = res[:half]
11        nums[1::2] = res[half:]
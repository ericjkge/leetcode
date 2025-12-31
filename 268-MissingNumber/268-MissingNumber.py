# Last updated: 12/31/2025, 10:14:27 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        nums.sort()
5
6        for i in range(n):
7            if i > 0 and nums[i] != nums[i - 1] + 1:
8                return nums[i] - 1
9        
10        if nums[0] != 0:
11            return 0
12
13        return n
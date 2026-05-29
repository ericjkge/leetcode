# Last updated: 5/28/2026, 8:42:06 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        nums_set = set(nums)
4        nums = list(nums_set)
5        nums.sort(reverse=True)
6
7        if len(nums) < 3:
8            return max(nums)
9        
10        return nums[2]
11
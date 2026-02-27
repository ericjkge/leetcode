# Last updated: 2/27/2026, 9:14:24 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        print(nums)
5        triplets = []
6
7        for i, num in enumerate(nums):
8            if i > 0 and num == nums[i - 1]:
9                continue
10            target = -num
11            left, right = i + 1, len(nums) - 1
12            while left < right:
13                if nums[left] + nums[right] > target:
14                    right -= 1
15                elif nums[left] + nums[right] < target:
16                    left += 1
17                else:
18                    triplets.append([num, nums[left], nums[right]])
19                    left += 1
20                    while left < right and nums[left] == nums[left - 1]:
21                        left += 1
22
23        return triplets
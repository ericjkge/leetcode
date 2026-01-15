# Last updated: 1/15/2026, 12:35:57 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        solutions = []
5        n = len(nums)
6
7        for i in range(n):
8            if i > 0 and nums[i] == nums[i - 1]:
9                continue
10            target = -nums[i]
11            left, right = i + 1, n - 1
12            while left < right:
13                if nums[left] + nums[right] < target:
14                    left += 1
15                elif nums[left] + nums[right] > target:
16                    right -= 1
17                else:
18                    solutions.append([nums[i], nums[left], nums[right]])
19                    left += 1
20                    while left < right and nums[left] == nums[left - 1]:
21                        left += 1
22
23        return solutions
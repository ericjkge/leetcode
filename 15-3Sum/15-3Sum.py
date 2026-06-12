# Last updated: 6/11/2026, 9:41:17 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4        nums.sort()
5
6        for i in range(len(nums)):
7            if i > 0 and nums[i] == nums[i - 1]:
8                continue
9
10            target = -nums[i]
11            left, right = i + 1, len(nums) - 1
12            while left < right:
13                if nums[left] + nums[right] > target:
14                    right -= 1
15                elif nums[left] + nums[right] < target:
16                    left += 1
17                else:
18                    ans.append([nums[i], nums[left], nums[right]])
19                    left += 1
20                    while left < right and nums[left] == nums[left - 1]:
21                        left += 1
22
23
24        return ans
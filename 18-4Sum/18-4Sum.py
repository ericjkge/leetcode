# Last updated: 6/27/2026, 3:43:56 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        ans = []
5
6        for i in range(len(nums)):
7            if i > 0 and nums[i] == nums[i - 1]:
8                continue
9            for j in range(i + 1, len(nums)):
10                if j > i + 1 and nums[j] == nums[j - 1]:
11                    continue
12                goal = target - (nums[i] + nums[j])
13                left, right = j + 1, len(nums) - 1
14                while left < right:
15                    if nums[left] + nums[right] < goal:
16                        left += 1
17                    elif nums[left] + nums[right] > goal:
18                        right -= 1
19                    else:
20                        ans.append([nums[i], nums[j], nums[left], nums[right]])
21                        left += 1
22                        while left < right and nums[left] == nums[left - 1]:
23                            left += 1
24
25        return ans
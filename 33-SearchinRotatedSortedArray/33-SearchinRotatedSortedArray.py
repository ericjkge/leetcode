# Last updated: 1/18/2026, 9:44:30 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left + 1 < right:
6            mid = (left + right) // 2
7            if nums[mid] > nums[left]:
8                if nums[left] <= target <= nums[mid]:
9                    right = mid
10                else:
11                    left = mid
12            else:
13                if nums[mid] <= target <= nums[right]:
14                    left = mid
15                else:
16                    right = mid
17        
18        if nums[left] == target:
19            return left
20        if nums[right] == target:
21            return right
22        return -1
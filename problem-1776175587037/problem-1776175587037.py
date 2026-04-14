# Last updated: 4/14/2026, 10:06:27 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4        while left + 1 < right:
5            mid = (left + right) // 2
6            if nums[mid] > target:
7                right = mid
8            else:
9                left = mid
10        
11        if nums[left] == target:
12            return left
13        elif nums[right] == target:
14            return right
15        return -1
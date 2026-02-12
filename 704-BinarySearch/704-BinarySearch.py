# Last updated: 2/12/2026, 11:51:19 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left + 1 < right:
6            mid = (left + right) // 2
7            if nums[mid] < target:
8                left = mid
9            else:
10                right = mid
11        
12        if nums[left] == target:
13            return left
14        elif nums[right] == target:
15            return right
16        return -1
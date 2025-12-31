# Last updated: 12/31/2025, 11:02:49 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left + 1 < right:
6            mid = (left + right) // 2
7            if nums[mid] > target:
8                right = mid
9            else:
10                left = mid
11        
12        if nums[left] == target:
13            return left
14        if nums[right] == target:
15            return right
16        return -1
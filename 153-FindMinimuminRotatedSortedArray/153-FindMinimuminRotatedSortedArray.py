# Last updated: 3/24/2026, 10:53:51 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4        while left + 1 < right:
5            mid = (left + right) // 2
6            if nums[mid] < nums[right]:
7                right = mid
8            else:
9                left = mid
10        
11        return min(nums[left], nums[right])
# Last updated: 12/23/2025, 1:49:10 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left + 1 < right:
6            mid = (left + right) // 2
7            if nums[mid] < nums[right]:
8                right = mid
9            else:
10                left = mid
11        
12        if nums[left] < nums[right]:
13            return nums[left]
14        return nums[right]
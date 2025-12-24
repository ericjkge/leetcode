# Last updated: 12/24/2025, 10:06:38 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 0, len(numbers) - 1
4
5        while left < right:
6            if numbers[left] + numbers[right] > target:
7                right -= 1
8            elif numbers[left] + numbers[right] < target:
9                left += 1
10            else:
11                return [left + 1, right + 1]
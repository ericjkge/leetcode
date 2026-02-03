# Last updated: 2/3/2026, 9:48:49 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 0, len(numbers) - 1
4
5        while left < right:
6            total = numbers[left] + numbers[right]
7            if total > target:
8                right -= 1
9            elif total < target:
10                left += 1
11            else:
12                return [left + 1, right + 1]
13    
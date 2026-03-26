# Last updated: 3/26/2026, 4:22:16 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 0, len(numbers) - 1
4        while left < right:
5            if numbers[left] + numbers[right] < target:
6                left += 1
7            elif numbers[left] + numbers[right] > target:
8                right -= 1
9            else:
10                return [left + 1, right + 1]
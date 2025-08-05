# Last updated: 8/6/2025, 12:07:47 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                break
            if total < target:
                left += 1
            else:
                right -= 1

        
        return [left + 1, right + 1]
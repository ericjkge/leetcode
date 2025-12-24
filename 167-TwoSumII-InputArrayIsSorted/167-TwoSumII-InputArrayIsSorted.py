# Last updated: 12/24/2025, 10:04:52 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        hashmap = {}
4
5        for i, num in enumerate(numbers):
6            remainder = target - num
7            if remainder in hashmap:
8                return [hashmap[remainder] + 1, i + 1]
9            hashmap[num] = i
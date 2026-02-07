# Last updated: 2/7/2026, 1:48:18 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for num in nums:
6            if num in seen:
7                return True
8            seen.add(num)
9
10        return False
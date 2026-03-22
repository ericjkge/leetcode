# Last updated: 3/22/2026, 9:41:20 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        total = 0
4        
5        for num in nums:
6            total ^= num
7        
8        return total
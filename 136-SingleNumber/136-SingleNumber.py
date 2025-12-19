# Last updated: 12/19/2025, 9:00:43 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        ans = 0
4        for num in nums:
5            ans ^= num
6        return ans
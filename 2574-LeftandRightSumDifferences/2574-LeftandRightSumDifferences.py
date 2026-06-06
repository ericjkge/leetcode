# Last updated: 6/6/2026, 12:17:29 AM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        total = sum(nums)
4        left = 0
5        res = []
6
7        for num in nums:
8            right = total - left - num
9            res.append(abs(left - right))
10            left += num
11
12        return res
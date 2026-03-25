# Last updated: 3/25/2026, 1:26:36 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        ans = maxp = minp = nums[0]
4
5        for num in nums[1:]:
6            maxt = maxp
7
8            maxp = max(maxt * num, num, num * minp)
9            minp = min(maxt * num, num, num * minp)
10            ans = max(ans, maxp)
11
12        return ans
# Last updated: 12/30/2025, 11:36:23 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [1] * n
5
6        prefix = 1
7        for i in range(n):
8            ans[i] = prefix
9            prefix *= nums[i]
10
11        suffix = 1
12        for j in range(n - 1, -1, -1):
13            ans[j] *= suffix
14            suffix *= nums[j]
15
16        return ans
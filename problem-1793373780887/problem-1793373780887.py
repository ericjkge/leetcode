# Last updated: 10/30/2026, 11:23:00 AM
1class Solution:
2    def productExceptSelf(self, nums: list[int]) -> list[int]:
3        prefix = [1]
4        suffix = [1]
5
6        for i in range(len(nums)):
7            prefix.append(prefix[-1] * nums[i])
8        
9        for j in range(len(nums) - 1, -1, -1):
10            suffix.append(suffix[-1] * nums[j])
11
12        res = []
13        for k in range(len(nums)):
14            res.append(prefix[k] * suffix[len(nums) - k - 1])
15        return res
16
17
18        
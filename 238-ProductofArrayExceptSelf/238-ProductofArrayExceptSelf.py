# Last updated: 12/30/2025, 11:26:59 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5
6        prefix = [nums[0]]
7        for i in range(1, n):
8            prefix.append(prefix[-1] * nums[i])
9
10        suffix = [nums[-1]]
11        for j in range(n - 2, -1, -1):
12            suffix.append(suffix[-1] * nums[j])
13        suffix = suffix[::-1]
14
15        for k in range(n):
16            pre = prefix[k - 1] if k - 1 >= 0 else 1
17            suf = suffix[k + 1] if k + 1 < n else 1
18            ans[k] = pre * suf
19
20        return ans
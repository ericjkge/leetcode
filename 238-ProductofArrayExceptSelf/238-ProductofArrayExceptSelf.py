# Last updated: 4/6/2026, 11:49:06 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = [1]
4        for n in nums:
5            prefix.append(prefix[-1] * n)
6        
7        suffix = [1]
8        for i in range(len(nums) - 1, -1, -1):
9            suffix.append(suffix[-1] * nums[i])
10        suffix = suffix[::-1]
11
12        prefix = prefix[1:]
13        suffix = suffix[:-1]
14
15        ans = [0] * len(nums)
16        for i in range(len(nums)):
17            left = prefix[i - 1] if i > 0 else 1
18            right = suffix[i + 1] if i < len(nums) - 1 else 1
19            ans[i] = left * right
20
21        return ans
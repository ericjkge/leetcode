# Last updated: 7/4/2026, 4:18:25 PM
1class Solution:
2    def maximumSum(self, nums: List[int]) -> int:
3        ans = 0
4        mapping = defaultdict(int)
5
6        for i, num in enumerate(nums):
7            total = sum(int(d) for d in str(num))
8            if total in mapping:
9                ans = max(ans, num + mapping[total])
10            mapping[total] = max(mapping[total], num)
11
12        return ans if ans else -1
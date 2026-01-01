# Last updated: 1/1/2026, 10:26:29 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        def count(target):
4            res = 0
5            for n in nums:
6                if n <= target:
7                    res += 1
8            return res
9
10        left, right = 0, len(nums) - 1
11        while left + 1 < right:
12            mid = (left + right) // 2
13            if count(mid) <= mid:
14                left = mid
15            else:
16                right = mid
17        
18        if count(left) > left:
19            return left
20        return right
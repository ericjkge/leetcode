# Last updated: 4/15/2026, 8:53:34 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        def num_below(target):
4            counter = 0
5            for num in nums:
6                if num <= target:
7                    counter += 1
8            return counter
9
10        left, right = 0, len(nums)
11        while left + 1 < right:
12            mid = (left + right) // 2
13            if num_below(mid) > mid:
14                right = mid
15            else:
16                left = mid
17        
18        if num_below(left) > left:
19            return left
20        return right
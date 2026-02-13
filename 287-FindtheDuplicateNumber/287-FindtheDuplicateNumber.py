# Last updated: 2/13/2026, 9:54:17 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        def counter(target):
4            count = 0
5            for num in nums:
6                if num <= target:
7                    count += 1
8            return count
9        
10        left, right = 1, max(nums)
11
12        while left + 1 < right:
13            mid = (left + right) // 2
14            if counter(mid) > mid:
15                right = mid
16            else:
17                left = mid
18        
19        if counter(left) > left:
20            return left
21        return right
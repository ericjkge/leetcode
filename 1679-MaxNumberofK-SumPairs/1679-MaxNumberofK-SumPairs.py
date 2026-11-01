# Last updated: 11/1/2026, 11:30:40 AM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        left, right = 0, len(nums) - 1
4        count = 0
5        nums.sort()
6
7        while left < right:
8            total = nums[left] + nums[right]
9            if total > k:
10                right -= 1
11            elif total < k:
12                left += 1
13            else:
14                count += 1
15                left += 1
16                right -= 1
17        
18        return count
# Last updated: 11/13/2026, 1:19:29 AM
1class Solution:
2    def longestOnes(self, nums: list[int], k: int) -> int:
3        left = right = 0
4        window = 0
5        longest = 0
6
7        while right < len(nums):
8            if nums[right] == 0:
9                window += 1
10            
11            while window > k:
12                if nums[left] == 0:
13                    window -= 1
14                left += 1
15            
16            longest = max(longest, right - left + 1)
17            right += 1
18        
19        return longest
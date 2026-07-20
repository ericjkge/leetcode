# Last updated: 7/19/2026, 9:00:46 PM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        left = right = 0
4        window = 0
5        ans = 0
6
7        while right < len(nums):
8            if nums[right] == 0:
9                window += 1
10            
11            while window > 1:
12                if nums[left] == 0:
13                    window -= 1
14                left += 1
15            
16            ans = max(ans, right - left)
17            right += 1
18        
19        return ans
# Last updated: 11/1/2026, 12:58:10 PM
1class Solution:
2    def longestSubarray(self, nums: list[int]) -> int:
3        left = right = 0
4        ans = 0
5        flag = 1
6
7        while right < len(nums):
8            if nums[right] != 1:
9                flag -= 1
10            
11            while flag < 0:
12                if nums[left] != 1:
13                    flag += 1
14                left += 1
15            
16            ans = max(ans, right - left)
17            right += 1
18        
19        return ans
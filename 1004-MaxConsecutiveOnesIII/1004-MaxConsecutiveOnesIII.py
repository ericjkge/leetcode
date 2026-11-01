# Last updated: 11/1/2026, 12:51:44 PM
1class Solution:
2    def longestOnes(self, nums: list[int], k: int) -> int:
3        left = right = 0
4        flips = k
5        ans = 0
6
7        while right < len(nums):
8            if nums[right] == 0:
9                flips -= 1
10
11            while flips < 0:
12                if nums[left] == 0:
13                    flips += 1
14                left += 1
15
16            ans = max(ans, right - left + 1)
17            right += 1
18            
19        return ans
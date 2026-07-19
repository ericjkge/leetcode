# Last updated: 7/19/2026, 10:08:46 AM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        left = right = 0
4        window = 0
5        mx = float("-inf")
6
7        while right < len(nums):
8            window += nums[right]
9            if right < k - 1:
10                right += 1
11                continue
12            
13            while right - left + 1 > k:
14                window -= nums[left]
15                left += 1
16            
17            mx = max(mx, window / k)
18            right += 1
19
20        return mx
21
22
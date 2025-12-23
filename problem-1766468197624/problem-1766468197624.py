# Last updated: 12/23/2025, 1:36:37 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        curr_max = curr_min = best = nums[0]
4
5        for num in nums[1:]:
6            temp_max = curr_max
7
8            curr_max = max(curr_max * num, num, curr_min * num)
9            curr_min = min(curr_min * num, num, temp_max * num)
10            best = max(best, curr_max)
11        
12        return best
13
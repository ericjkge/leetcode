# Last updated: 6/24/2026, 10:59:33 PM
1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        ans = 0
4
5        for i in range(len(nums)):
6            count = 0
7            for j in range(i, len(nums)):
8                if nums[j] == target:
9                    count += 1
10                
11                if 2 * count > (j - i + 1):
12                    ans += 1
13        
14        return ans
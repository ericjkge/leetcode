# Last updated: 7/2/2026, 12:25:14 AM
1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3        def atMost(n):
4            ans = left = odds = 0
5            for right in range(len(nums)):
6                odds += nums[right] % 2
7                while odds > n:
8                    odds -= nums[left] % 2
9                    left += 1
10                ans += right - left + 1
11            return ans
12
13        return atMost(k) - atMost(k - 1)
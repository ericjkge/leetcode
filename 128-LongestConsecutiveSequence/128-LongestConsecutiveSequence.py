# Last updated: 8/6/2025, 11:21:15 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        
        ans = 0
        for n in seen:
            if n - 1 not in seen:
                streak = 1
                while n + 1 in seen:
                    streak += 1
                    n = n + 1
                ans = max(ans, streak)

        return ans
# Last updated: 7/8/2025, 10:58:49 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for _, freq in counter.items():
            ans += freq * (freq - 1) // 2
        return ans
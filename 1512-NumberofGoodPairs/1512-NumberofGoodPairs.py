# Last updated: 7/4/2025, 2:33:20 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for _, freq in counter.items():
            ans += freq * (freq - 1) // 2

        return ans
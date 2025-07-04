# Last updated: 7/4/2025, 10:51:43 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        return sum(freq for freq in count.values() if freq == max_freq)

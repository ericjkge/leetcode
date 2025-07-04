# Last updated: 7/4/2025, 10:51:02 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        return sum(count[key] for key in count if count[key] == max_freq)

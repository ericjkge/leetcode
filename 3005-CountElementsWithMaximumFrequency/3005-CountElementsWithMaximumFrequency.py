# Last updated: 7/4/2025, 10:50:42 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        total = 0
        for key in count:
            if count[key] == max_freq:
                total += count[key]
        return total

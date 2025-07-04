# Last updated: 7/4/2025, 11:33:16 AM
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict()
        max_length = 0
        left = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length

        
# Last updated: 7/4/2025, 4:03:47 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_val = 0
        total = 0
        left = 0
        counter = defaultdict(int)
        for right in range(len(nums)):
            counter[nums[right]] += 1
            total += nums[right]
            while counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                total -= nums[left]
                left += 1
            max_val = max(max_val, total)
        
        return max_val
# Last updated: 9/17/2025, 12:29:56 AM
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hashmap = {0: -1}
        longest = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in hashmap:
                longest = max(longest, i - hashmap[prefix - k])
            if prefix not in hashmap:
                hashmap[prefix] = i
            
        return longest

        # [1, 0, 5, 3, 6]
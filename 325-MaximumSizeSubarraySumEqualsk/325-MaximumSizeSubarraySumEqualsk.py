# Last updated: 7/27/2025, 10:10:04 PM
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hashmap = {0: -1}
        prefix = 0
        ans = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in hashmap:
                ans = max(ans, i - hashmap[prefix - k])
            if prefix not in hashmap:
                hashmap[prefix] = i
        
        return ans
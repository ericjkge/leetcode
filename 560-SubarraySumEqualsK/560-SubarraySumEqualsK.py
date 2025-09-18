# Last updated: 9/18/2025, 12:04:30 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hashmap = {0:1}
        ans = 0

        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in hashmap:
                ans += hashmap[prefix - k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return ans

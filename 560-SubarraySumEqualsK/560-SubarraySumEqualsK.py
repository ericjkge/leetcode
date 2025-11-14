# Last updated: 11/14/2025, 12:17:21 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hashmap = {0:1}
        ans = 0

        for num in nums:
            prefix += num
            if prefix - k in hashmap:
                ans += hashmap[prefix - k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        return ans
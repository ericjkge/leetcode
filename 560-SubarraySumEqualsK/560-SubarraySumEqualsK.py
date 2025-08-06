# Last updated: 8/6/2025, 7:29:47 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hashmap = {0: 1}
        ans = 0

        for num in nums:
            prefix += num
            if prefix - k in hashmap:
                ans += hashmap[prefix - k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return ans
# Last updated: 7/4/2025, 3:42:47 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1 # sum 0 seen once
        ans = 0
        prefix = 0
        for num in nums:
            prefix += num
            ans += hashmap[prefix - goal]
            hashmap[prefix] += 1
        
        return ans
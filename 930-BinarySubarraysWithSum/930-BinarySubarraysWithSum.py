# Last updated: 7/4/2025, 3:45:20 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        prefix = ans = 0
        count[0] = 1
        for num in nums:
            prefix += num
            ans += count[prefix - goal]
            count[prefix] += 1
        
        return ans
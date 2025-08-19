# Last updated: 8/19/2025, 11:14:32 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0

        for num in nums:
            prefix += num
            ans += freq[prefix - goal]
            freq[prefix] += 1
        
        return ans
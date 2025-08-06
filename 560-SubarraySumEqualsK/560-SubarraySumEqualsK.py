# Last updated: 8/6/2025, 7:26:49 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0, nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        counter = 0
        seen = {0: 1}
        for p in prefix[1:]:
            if p - k in seen:
                counter += seen[p - k]
            seen[p] = seen.get(p, 0) + 1
        
        return counter
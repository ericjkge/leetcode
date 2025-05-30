# Last updated: 5/30/2025, 12:07:48 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        
        for i in range(k, len(nums)):
            curr -= nums[i-k]
            curr += nums[i]
            ans = max(ans, curr)
        
        return ans/k
# Last updated: 7/2/2025, 5:23:01 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix *= nums[i]
        
        return ans
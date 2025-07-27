# Last updated: 7/27/2025, 11:51:37 PM
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

# Time: O(n)
# Space: O(1) (ignore ans)
# Last updated: 7/27/2025, 11:51:45 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])

        suffix = [1] * len(nums)
        suffix[len(nums) - 1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        ans = []
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < len(nums) - 1 else 1
            ans.append(left * right)
        
        return ans
# Time: O(n)
# Space: O(1) (ignore ans)
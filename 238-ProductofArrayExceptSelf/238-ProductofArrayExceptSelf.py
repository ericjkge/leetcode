# Last updated: 7/2/2025, 5:10:37 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = []
        suffix = []

        curr = 1
        for num in nums:
            curr *= num
            prefix.append(curr)
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            suffix.append(curr)
        
        suffix = suffix[::-1]

        print(prefix, suffix)

        ans.append(suffix[1])
        for i in range(1, len(nums) - 1):
            ans.append(prefix[i-1] * suffix[i+1])
        ans.append(prefix[len(nums) - 2])
        return ans



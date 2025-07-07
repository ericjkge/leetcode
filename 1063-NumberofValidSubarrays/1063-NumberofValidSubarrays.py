# Last updated: 7/7/2025, 11:12:07 AM
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                j = stack.pop()
                ans += i - j
            stack.append(i)
        
        while stack:
            j = stack.pop()
            ans += len(nums) - j
        
        return ans
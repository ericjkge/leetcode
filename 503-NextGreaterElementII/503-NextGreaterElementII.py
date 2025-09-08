# Last updated: 9/8/2025, 6:04:39 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            x = nums[i % n]
            while stack and nums[stack[-1]] < x:
                ans[stack.pop()] = x
            if i < n:
                stack.append(i)
        
        return ans

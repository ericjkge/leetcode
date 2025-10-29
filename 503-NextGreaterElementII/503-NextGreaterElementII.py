# Last updated: 10/29/2025, 8:56:46 AM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nxt = [-1] * len(nums)

        for _ in range(2):
            for i, n in enumerate(nums):
                while stack and nums[stack[-1]] < n:
                    nxt[stack.pop()] = n
                stack.append(i)
        
        return nxt
# Last updated: 7/7/2025, 12:13:22 PM
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and len(stack) + len(nums) - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        
        return stack
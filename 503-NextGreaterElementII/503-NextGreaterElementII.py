# Last updated: 10/29/2025, 9:04:56 AM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        nxt = [-1] * n

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                nxt[stack.pop()] = num
            if i < n:
                stack.append(i)
        
        return nxt
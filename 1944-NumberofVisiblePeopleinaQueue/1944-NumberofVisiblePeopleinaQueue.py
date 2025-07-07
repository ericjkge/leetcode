# Last updated: 7/7/2025, 12:54:54 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * (len(heights))
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            counter = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                counter += 1
            if stack:
                counter += 1
            ans[i] = counter
            stack.append(heights[i])
        return ans

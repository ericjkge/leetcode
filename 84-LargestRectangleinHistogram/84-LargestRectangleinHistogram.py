# Last updated: 6/30/2025, 11:01:43 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store index, height
        ans = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                ans = max(ans, (i - index) * height)
                start = index
            stack.append((start, h))
        
        for start, height in stack:
            ans = max(ans, (len(heights) - start) * height)

        return ans
        

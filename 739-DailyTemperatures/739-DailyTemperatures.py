# Last updated: 9/7/2025, 9:30:48 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        
        return ans
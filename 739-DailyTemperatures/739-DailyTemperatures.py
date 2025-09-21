# Last updated: 9/21/2025, 12:58:19 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]
        ans = [0] * n

        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        
        return ans

# Last updated: 12/28/2025, 11:35:41 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        n = len(temperatures)
4        stack = []
5        ans = [0] * n
6
7        for i in range(n):
8            while stack and temperatures[stack[-1]] < temperatures[i]:
9                index = stack.pop()
10                ans[index] = i - index
11            stack.append(i)
12        
13        return ans
# Last updated: 2/7/2026, 2:07:44 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        answer = [0] * len(temperatures)
5
6        for i, temp in enumerate(temperatures):
7            while stack and temp > temperatures[stack[-1]]:
8                index = stack.pop()
9                answer[index] = i - index
10            stack.append(i)
11
12        return answer
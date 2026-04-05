# Last updated: 4/5/2026, 10:35:39 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        answer = [0] * len(temperatures)
5
6        for i in range(len(temperatures)):
7            t = temperatures[i]
8            while stack and t > temperatures[stack[-1]]:
9                j = stack.pop()
10                answer[j] = i - j
11            stack.append(i)
12
13        return answer
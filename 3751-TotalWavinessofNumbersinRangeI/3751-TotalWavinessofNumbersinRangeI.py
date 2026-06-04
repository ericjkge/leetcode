# Last updated: 6/3/2026, 9:38:49 PM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        count = 0
4
5        for num in range(num1, num2 + 1):
6            if num < 100:
7                continue
8
9            s = str(num)
10            for i in range(1, len(s) - 1):
11                if s[i] > s[i - 1] and s[i] > s[i + 1]:
12                    count += 1
13                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
14                    count += 1
15        
16        return count
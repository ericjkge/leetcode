# Last updated: 1/19/2026, 12:15:29 PM
1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        m, n = len(num1), len(num2)
7        res = [0] * (m + n)
8
9        for i in range(m - 1, -1, -1):
10            for j in range(n - 1, -1, -1):
11                prod = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
12                s = prod + res[i + j + 1]
13
14                res[i + j + 1] = s % 10
15                res[i + j] += s // 10
16        
17        i = 0
18        while i < len(res) and res[i] == 0:
19            i += 1
20
21        return "".join(str(x) for x in res[i:])
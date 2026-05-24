# Last updated: 5/24/2026, 10:54:05 AM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        curNum = 0
5        curString = ""
6
7        for char in s:
8            if char.isdigit():
9                curNum = curNum * 10 + int(char)
10            elif char == "[":
11                stack.append((curNum, curString))
12                curNum = 0
13                curString = ""
14            elif char == "]":
15                repeats, prevString = stack.pop()
16                curString = prevString + curString * repeats
17            else:
18                curString += char
19        
20        return curString
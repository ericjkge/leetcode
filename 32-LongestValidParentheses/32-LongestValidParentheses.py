# Last updated: 7/15/2026, 10:54:33 PM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1] # top is last remaining unmatched
4        longest = 0
5
6        for i in range(len(s)):
7            if s[i] == "(":
8                stack.append(i)
9            else:
10                stack.pop()
11
12                if not stack:
13                    stack.append(i)
14                else:
15                    longest = max(longest, i - stack[-1])
16        
17        return longest
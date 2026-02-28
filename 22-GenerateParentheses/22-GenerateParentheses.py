# Last updated: 2/28/2026, 10:07:10 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        ans = []
4
5        def backtrack(open, closed, path):
6            if len(path) == n * 2:
7                ans.append("".join(path))
8                return
9            
10            if open > 0:
11                path.append("(")
12                backtrack(open - 1, closed, path)
13                path.pop()
14
15            if closed > open:
16                path.append(")")
17                backtrack(open, closed - 1, path)
18                path.pop()
19
20        backtrack(n, n, [])
21        return ans
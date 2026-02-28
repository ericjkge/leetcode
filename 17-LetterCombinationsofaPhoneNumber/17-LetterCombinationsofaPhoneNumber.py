# Last updated: 2/28/2026, 9:44:57 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        mappings = {
4            "2":"abc",
5            "3":"def",
6            "4":"ghi",
7            "5":"jkl",
8            "6":"mno",
9            "7":"pqrs",
10            "8":"tuv",
11            "9":"wxyz"
12        }
13
14        ans = []
15
16        def backtrack(index, path):
17            if len(path) == len(digits):
18                ans.append("".join(path))
19                return
20            
21            for char in mappings[digits[index]]:
22                path.append(char)
23                backtrack(index + 1, path)
24                path.pop()
25        
26        backtrack(0, [])
27        return ans
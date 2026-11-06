# Last updated: 11/6/2026, 6:21:11 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> list[str]:
3        combinations = []
4        mapping = {
5            "2": "abc",
6            "3": "def",
7            "4": "ghi",
8            "5": "jkl",
9            "6": "mno",
10            "7": "pqrs",
11            "8": "tuv",
12            "9": "wxyz"
13        }
14
15        def backtrack(index, path):
16            if index == len(digits):
17                combinations.append("".join(path))
18                return
19            
20            for letter in mapping[digits[index]]:
21                path.append(letter)
22                backtrack(index + 1, path)
23                path.pop()
24        
25        backtrack(0, [])
26        return combinations
27
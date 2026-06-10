# Last updated: 6/9/2026, 8:24:13 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        @cache
4        def dp(i):
5            if i == len(s):
6                return True
7
8            if i > len(s):
9                return False
10            
11            valid = False
12            for word in wordDict:
13                if s[i:i + len(word)] == word:
14                    if dp(i + len(word)):
15                        valid = True
16
17            return valid
18
19        return dp(0)
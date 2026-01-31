# Last updated: 1/31/2026, 1:37:38 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        @cache
4        def dp(i):
5            if i == len(s):
6                return True
7
8            for word in wordDict:
9                length = len(word)
10                if s[i:i + length] == word:
11                    if dp(i + length):
12                        return True
13            
14            return False
15
16        return dp(0)    
# Last updated: 12/21/2025, 9:15:56 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordSet = set(wordDict)
4        n = len(s)
5
6        @cache
7        def dp(i):
8            if i == n:
9                return True
10
11            if i > n:
12                return False
13
14            for word in wordSet:
15                if s[i:i + len(word)] == word:
16                    if dp(i + len(word)):
17                        return True
18            
19            return False
20
21        return dp(0)
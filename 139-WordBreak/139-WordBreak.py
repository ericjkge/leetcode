# Last updated: 6/9/2025, 11:27:56 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp) and s[i:i + len(word)] == word:
                    print(s[i:i + len(word)])
                    dp[i] = dp[i + len(word)]
                if dp[i] == True:
                    break
        
        return dp[0]
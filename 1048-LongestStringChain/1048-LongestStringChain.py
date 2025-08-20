# Last updated: 8/20/2025, 10:16:35 PM
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        S = set(words)  # O(N)
        
        @cache
        def dp(w):
            best = 1
            # delete one char at each position
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                if prev in S:
                    best = max(best, 1 + dp(prev))
            return best

        return max(dp(w) for w in S)
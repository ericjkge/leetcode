# Last updated: 8/22/2025, 9:14:53 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1
        
        ans = ""
        for i in range(len(s)):
            even_length = expand(i, i + 1)
            if even_length > len(ans):
                dist = even_length // 2
                ans = s[i - dist + 1:i + dist + 1]
            odd_length = expand(i, i)
            if odd_length > len(ans):
                dist = odd_length // 2
                ans = s[i - dist:i + dist + 1]
        
        return ans
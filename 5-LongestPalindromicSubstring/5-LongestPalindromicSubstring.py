# Last updated: 8/12/2025, 9:59:03 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return j - i - 1

        ans = ""
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > len(ans):
                dist = odd_length // 2
                ans = s[i - dist: i + dist + 1]
            even_length = expand(i, i + 1)
            if even_length > len(ans):
                dist = even_length // 2
                ans = s[i - dist + 1: i + dist + 1]
        
        return ans

# Last updated: 6/8/2025, 6:53:31 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_substring = expand(i, i)
            if odd_substring > ans[1] - ans[0] + 1:
                dist = odd_substring // 2
                ans = [i - dist, i + dist]
            even_substring = expand(i, i + 1)
            if even_substring > ans[1] - ans[0] + 1:
                dist = even_substring // 2 - 1
                ans = [i - dist, i + 1 + dist]
        
        i, j = ans

        return s[i:j + 1]
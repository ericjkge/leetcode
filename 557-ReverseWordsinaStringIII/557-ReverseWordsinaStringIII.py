# Last updated: 7/3/2025, 6:13:15 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        start = 0

        for end in range(len(s) + 1):
            if end == len(s) or chars[end] == " ":
                l, r = start, end - 1
                while l < r:
                    chars[l], chars[r] = chars[r], chars[l]
                    l += 1
                    r -= 1
                start = end + 1

        return "".join(chars)
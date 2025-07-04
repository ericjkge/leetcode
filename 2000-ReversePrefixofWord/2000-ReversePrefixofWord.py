# Last updated: 7/3/2025, 10:36:25 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chars = list(word)
        start = end = 0
        for i in range(len(word)):
            if chars[i] == ch:
                end = i
                while start < end:
                    chars[start], chars[end] = chars[end], chars[start]
                    start += 1
                    end -= 1
                break

        return "".join(chars)
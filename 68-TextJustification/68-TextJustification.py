# Last updated: 8/29/2025, 4:24:27 PM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, n = 0, len(words)
        ans = []

        while i < n:
            j = i
            line_len = 0

            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            line_words = words[i:j]
            spaces = maxWidth - line_len
            gaps = j - i - 1
            line_parts = []

            if j == n or gaps == 0:
                line_parts.append(" ".join(line_words))
                line_parts.append(" " * (spaces - gaps))
            else:
                avg, extra = divmod(spaces, gaps)
                for k in range(len(line_words[:-1])):
                    line_parts.append(line_words[k])
                    line_parts.append(" " * (avg + (1 if k < extra else 0)))
                line_parts.append(line_words[-1])
            ans.append("".join(line_parts))
            i = j

        return ans
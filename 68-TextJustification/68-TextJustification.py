# Last updated: 8/23/2025, 11:38:26 PM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i, n = 0, len(words)

        while i < n:
            j = i
            line_len = 0
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            line_words = words[i:j]
            gaps = len(line_words) - 1
            spaces = maxWidth - line_len
            
            if j == n or gaps == 0: # last line or single word
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                avg, extra = divmod(spaces, gaps)
                parts = []
                for k, w in enumerate(line_words[:-1]):
                    parts.append(w)
                    parts.append(" " * (avg + (1 if k < extra else 0)))
                parts.append(line_words[-1])
                line = "".join(parts)
            ans.append(line)
            i = j

        return ans
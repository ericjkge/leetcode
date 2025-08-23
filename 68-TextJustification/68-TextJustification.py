# Last updated: 8/23/2025, 11:00:24 PM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)

        def justify(array, last, chars):
            chars = chars - len(array)
            numSpaces = maxWidth - chars
            if last:
                return " ".join(array) + " " * (maxWidth - chars - len(array) + 1)
            if len(array) == 1:
                return array[0] + " " * numSpaces
            else:
                m = len(array) - 1
                remainder = 0
                if m and numSpaces % m != 0:
                    remainder = numSpaces % m
                avgSpaces = numSpaces // m
                res = ""
                for i in range(0, m):
                    if remainder:
                        res += (array[i] + " " * (avgSpaces + 1))
                        remainder -= 1
                    else:
                        res += (array[i] + " " * (avgSpaces))
                res += array[m]
                return res

        ans = []
        curr = []
        chars = 0
        for i in range(n):
            if chars + len(words[i]) <= maxWidth:
                curr.append(words[i])
                chars += len(words[i]) + 1
                if i == n - 1:
                    print(curr, chars)
                    ans.append(justify(curr, True, chars))
            else:
                print(curr, chars)
                ans.append(justify(curr, False, chars))
                curr = [words[i]]
                chars = len(words[i]) + 1
                if i == n - 1:
                    print(curr, chars)
                    ans.append(justify(curr, True, chars))
        return ans


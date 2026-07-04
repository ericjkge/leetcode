# Last updated: 7/4/2026, 12:46:52 PM
1class Solution:
2    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
3        res = []
4        line = [words[0]]
5        length = len(words[0])
6
7        def makeLeft(line, length):
8            gap = maxWidth - length
9            return " ".join(line) + " " * gap
10
11        def makeLine(line, length):
12            if len(line) == 1:
13                return makeLeft(line, length)
14
15            res = []
16            gap = maxWidth - length
17            quo, rem = divmod(gap, len(line) - 1)
18            for word in line[:-1]:
19                if rem:
20                    res.append(word + " " * (quo + 2))
21                    rem -= 1
22                else:
23                    res.append(word + " " * (quo + 1))
24            res.append(line[-1])
25            return "".join(res)
26
27        for word in words[1:]:
28            if length + len(word) + 1 <= maxWidth:
29                line.append(word)
30                length += len(word) + 1
31            else:
32                res.append(makeLine(line, length))
33                line = [word]
34                length = len(word)
35
36        res.append(makeLeft(line, length))
37        return res
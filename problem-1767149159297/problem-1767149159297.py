# Last updated: 12/31/2025, 10:45:59 AM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        res = ""
6
7        for s in strs:
8            res += str(len(s))
9            res += "#"
10            res += s
11
12        return res
13
14    def decode(self, s: str) -> List[str]:
15        """Decodes a single string to a list of strings.
16        """
17        res = []
18        i = 0
19        while i < len(s):
20            j = i
21
22            while s[j] != "#":
23                j += 1
24
25            length = int(s[i:j])
26            res.append(s[j + 1: j + 1 + length])
27            
28            i = j + 1 + length
29        
30        return res
31
32        5#Hello5#World
33
34
35# Your Codec object will be instantiated and called as such:
36# codec = Codec()
37# codec.decode(codec.encode(strs))
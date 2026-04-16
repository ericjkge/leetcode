# Last updated: 4/15/2026, 9:03:06 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        encoding = []
6        for s in strs:
7            encoding.append(str(len(s)) + "#" + s)
8        return "".join(encoding)
9
10    def decode(self, s: str) -> List[str]:
11        """Decodes a single string to a list of strings.
12        """
13        decoding = []
14        index = 0
15        while index < len(s):
16            length = 0
17            while s[index].isalnum():
18                length *= 10
19                length += int(s[index])
20                index += 1
21            index += 1 # Skip "#"
22            decoding.append(s[index:index + length])
23            index = index + length
24        return decoding
25
26
27# Your Codec object will be instantiated and called as such:
28# codec = Codec()
29# codec.decode(codec.encode(strs))
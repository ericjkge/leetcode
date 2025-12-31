# Last updated: 12/31/2025, 10:29:48 AM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        res = []
6        for s in strs:
7            res.append(s)
8        return "☃".join(res)
9
10    def decode(self, s: str) -> List[str]:
11        """Decodes a single string to a list of strings.
12        """
13        strings = s.split("☃")
14        return strings
15
16
17# Your Codec object will be instantiated and called as such:
18# codec = Codec()
19# codec.decode(codec.encode(strs))
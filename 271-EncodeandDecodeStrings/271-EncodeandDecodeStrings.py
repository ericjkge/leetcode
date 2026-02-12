# Last updated: 2/12/2026, 1:21:01 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        encoding = []
6
7        for s in strs:
8            encoding.append(str(len(s)) + "#" + s)
9
10        return "".join(encoding)
11
12    5#63/Rc1#h13#BmI3FS~J9#vmk
13
14    def decode(self, s: str) -> List[str]:
15        """Decodes a single string to a list of strings.
16        """
17        decoding = []
18        i = 0
19
20        while i < len(s):
21            start = i
22            while s[i] != "#":
23                i += 1
24            length = int(s[start:i])
25            string = s[i + 1: i + 1 + length]
26            i = i + 1 + length
27            decoding.append(string)
28        
29        return decoding
30
31
32# Your Codec object will be instantiated and called as such:
33# codec = Codec()
34# codec.decode(codec.encode(strs))
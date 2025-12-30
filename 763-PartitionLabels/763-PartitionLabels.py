# Last updated: 12/31/2025, 12:28:26 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        last = {char: i for i, char in enumerate(s)}
4
5        partitions = []
6        start = end = 0
7
8        for i, char in enumerate(s):
9            end = max(end, last[char])
10
11            if i == end:
12                partitions.append(end - start + 1)
13                start = i + 1
14
15        return partitions
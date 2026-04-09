# Last updated: 4/9/2026, 9:55:44 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        last = {k:i for i, k in enumerate(s)}
4        partitions = []
5        start = end = 0
6
7        for i, char in enumerate(s):
8            end = max(end, last[char])
9
10            if i == end:
11                partitions.append(end - start + 1)
12                start = i + 1
13
14        return partitions
15
16
# Last updated: 2/9/2026, 5:38:30 PM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        last = {char:i for i, char in enumerate(s)}
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
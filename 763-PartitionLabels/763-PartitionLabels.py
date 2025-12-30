# Last updated: 12/31/2025, 12:23:32 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        last = {char: i for i, char in enumerate(s)}
4
5        left = right = 0
6        partitions = []
7        counter = 0
8
9        while right < len(s):
10            right = last[s[right]]
11            counter += 1
12            while left < right:
13                right = max(right, last[s[left]])
14                counter += 1
15                left += 1
16            right += 1
17            partitions.append(counter)
18            counter = -1
19
20        return partitions
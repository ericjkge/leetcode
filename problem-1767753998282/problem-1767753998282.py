# Last updated: 1/7/2026, 10:46:38 AM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        if len(hand) % groupSize != 0:
4            return False
5        
6        count = Counter(hand)
7        keys = list(count.keys())
8        keys.sort()
9
10        for key in keys:
11            while count[key] > 0:
12                curr = key
13                for _ in range(groupSize - 1):
14                    if count[curr + 1] == 0:
15                        return False
16                    count[curr + 1] -= 1
17                    curr += 1
18                count[key] -= 1
19
20        return True
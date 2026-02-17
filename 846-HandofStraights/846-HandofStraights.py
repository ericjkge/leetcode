# Last updated: 2/17/2026, 8:59:32 AM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        if len(hand) % groupSize != 0:
4            return False
5        
6        freqs = Counter(hand)
7        keys = list(freqs.keys())
8        keys.sort()
9
10        for key in keys:
11            while freqs[key] != 0:
12                for i in range(groupSize):
13                    if freqs[key + i] == 0:
14                        return False
15                    freqs[key + i] -= 1
16        
17        return True
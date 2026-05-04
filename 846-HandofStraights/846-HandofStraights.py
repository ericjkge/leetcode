# Last updated: 5/4/2026, 12:15:29 PM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        if len(hand) % groupSize != 0:
4            return False
5        
6        freqs = Counter(hand)
7        keys = sorted(freqs.keys())
8
9        for key in keys:
10            while freqs[key] != 0:
11                for i in range(groupSize):
12                    if freqs[key + i] == 0:
13                        return False
14                    freqs[key + i] -= 1
15        
16        return True
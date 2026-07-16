# Last updated: 7/15/2026, 10:27:58 PM
1class Solution:
2    def knightDialer(self, n: int) -> int:
3        MOD = 10 ** 9 + 7
4        moves = {
5            0: [4, 6],
6            1: [6, 8],
7            2: [7, 9],
8            3: [4, 8],
9            4: [0, 3, 9],
10            5: [],
11            6: [0, 1, 7],
12            7: [2, 6],
13            8: [1, 3],
14            9: [2, 4]
15        }
16
17        @cache
18        def dp(i, j): # number, length
19            if j == n:
20                return 1
21            
22            total = 0
23            for move in moves[i]:
24                total += dp(move, j + 1)
25            return total
26        
27        return sum(dp(i, 1) for i in range(10)) % MOD
28
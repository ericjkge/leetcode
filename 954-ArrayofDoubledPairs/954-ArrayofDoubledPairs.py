# Last updated: 6/29/2026, 9:25:16 PM
1class Solution:
2    def canReorderDoubled(self, arr: List[int]) -> bool:
3        freqs = Counter(arr)
4        arr.sort(key=lambda x: abs(x))
5
6        for num in arr:
7            required = freqs[num]
8            if freqs[2 * num] < required:
9                return False
10            freqs[num] -= required
11            freqs[2 * num] -= required
12        
13        return True
# Last updated: 5/26/2026, 7:56:48 AM
1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        n = len(A)
4        res = [0] * n
5        count = defaultdict(int)
6        common = 0
7
8        for i in range(n):
9            count[A[i]] += 1
10            if count[A[i]] == 2:
11                common += 1
12            count[B[i]] += 1
13            if count[B[i]] == 2:
14                common += 1
15            res[i] = common
16        
17        return res
18
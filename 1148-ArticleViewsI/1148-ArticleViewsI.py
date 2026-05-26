# Last updated: 5/26/2026, 7:53:14 AM
1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        seta = set()
4        setb = set()
5        res = [0] * len(A)
6
7        for i in range(len(A)):
8            seta.add(A[i])
9            setb.add(B[i])
10            res[i] = len(seta & setb)
11        
12        return res
# Last updated: 7/4/2026, 3:07:38 PM
1class Solution:
2    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
3        occurrences = []
4        res = []
5
6        for i, num in enumerate(nums):
7            if num == x:
8                occurrences.append(i)
9
10        for query in queries:
11            if query - 1 < len(occurrences):
12                res.append(occurrences[query - 1])
13            else:
14                res.append(-1)
15
16        return res
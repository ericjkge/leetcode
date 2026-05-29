# Last updated: 5/28/2026, 8:46:05 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        first = second = third = float("-inf")
4
5        for num in nums:
6            if num == first or num == second or num == third:
7                continue
8
9            if num > first:
10                third = second
11                second = first
12                first = num
13            elif num > second:
14                third = second
15                second = num
16            elif num > third:
17                third = num
18            
19        return third if third != float("-inf") else first
20
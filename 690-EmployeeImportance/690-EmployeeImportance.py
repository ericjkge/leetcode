# Last updated: 8/9/2026, 12:21:25 AM
1"""
2# Definition for Employee.
3class Employee:
4    def __init__(self, id: int, importance: int, subordinates: List[int]):
5        self.id = id
6        self.importance = importance
7        self.subordinates = subordinates
8"""
9
10class Solution:
11    def getImportance(self, employees: List['Employee'], id: int) -> int:
12        mapping = {employee.id:employee for employee in employees}
13
14        def dfs(employee):
15            total = employee.importance
16            for subordinate in employee.subordinates:
17                total += dfs(mapping[subordinate])
18            return total
19
20        for employee in employees:
21            if employee.id == id:
22                return dfs(employee)
23
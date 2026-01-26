# Last updated: 1/26/2026, 1:01:54 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m, n  = len(matrix), len(matrix[0])
4        left, right = 0, m * n - 1
5
6        while left + 1 < right:
7            mid = (left + right) // 2
8            if matrix[mid // n][mid % n] > target:
9                right = mid
10            else:
11                left = mid
12        
13        if matrix[left // n][left % n] == target or matrix[right // n][right % n] == target:
14            return True
15        return False
16
17
# Last updated: 5/23/2026, 7:25:48 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        p1 = m - 1
7        p2 = n - 1
8        p3 = m + n - 1
9
10        while p1 >= 0 and p2 >= 0:
11            if nums1[p1] > nums2[p2]:
12                nums1[p3] = nums1[p1]
13                p1 -= 1
14            else:
15                nums1[p3] = nums2[p2]
16                p2 -= 1
17            p3 -= 1
18
19        while p2 >= 0:
20            nums1[p3] = nums2[p2]
21            p2 -= 1
22            p3 -= 1
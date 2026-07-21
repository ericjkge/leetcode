# Last updated: 7/20/2026, 9:48:41 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        l1, l2 = [], []
4
5        for num in set(nums1):
6            if num not in nums2:
7                l1.append(num)
8        
9        for num in set(nums2):
10            if num not in nums1:
11                l2.append(num)
12            
13        return l1, l2
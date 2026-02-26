# Last updated: 2/26/2026, 9:00:47 AM
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        mapping = {}
9
10        for i, num in enumerate(nums):
11            complement = target - num
12            if complement in mapping:
13                return [mapping[complement], i]
14            mapping[num] = i
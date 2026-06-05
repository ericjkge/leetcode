# Last updated: 6/4/2026, 9:35:01 PM
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
13                return (mapping[complement], i)
14            
15            mapping[num] = i
16        
17        return None
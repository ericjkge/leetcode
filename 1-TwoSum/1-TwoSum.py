# Last updated: 1/13/2026, 11:31:56 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        hashmap = {}
9        for i in range(len(nums)):
10            complement = target - nums[i]
11            if complement in hashmap:
12                return [hashmap[complement], i]
13            hashmap[nums[i]] = i
14
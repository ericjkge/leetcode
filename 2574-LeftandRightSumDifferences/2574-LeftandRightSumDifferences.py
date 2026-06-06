# Last updated: 6/6/2026, 12:10:05 AM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        leftSum = []
4        leftPrefix = 0
5        rightSum = [0] * len(nums)
6        rightPrefix = 0
7
8        for i in range(len(nums)):
9            leftSum.append(leftPrefix)
10            leftPrefix += nums[i]
11        
12        for j in range(len(nums) - 1, -1, -1):
13            rightSum[j] = rightPrefix
14            rightPrefix += nums[j]
15
16        return [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
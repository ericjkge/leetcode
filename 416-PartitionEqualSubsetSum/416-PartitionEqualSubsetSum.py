# Last updated: 2/17/2026, 9:18:05 AM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        if sum(nums) % 2 != 0:
4            return False
5        
6        target = sum(nums) // 2
7        nums.sort()
8
9        @cache
10        def dp(i, j): # position, sum
11            if j == target:
12                return True
13            
14            # if j > target:
15            #     return False
16
17            for k in range(i, len(nums)):
18                if dp(k + 1, j + nums[i]):
19                    return True
20            
21            return False
22        
23        return dp(0, 0)
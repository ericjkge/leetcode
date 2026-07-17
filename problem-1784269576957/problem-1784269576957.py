# Last updated: 7/16/2026, 11:26:16 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = [1]
4        for num in nums:
5            prefix.append(prefix[-1] * num)
6        
7        suffix = [1]
8        for num in nums[::-1]:
9            suffix.append(suffix[-1] * num)
10        suffix.reverse()
11        
12        res = [0] * len(nums)
13        for i in range(len(nums)):
14            res[i] = prefix[i] * suffix[i + 1]
15        
16        return res
17
18
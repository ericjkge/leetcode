# Last updated: 2/9/2026, 4:43:47 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = [nums[0]]
4        for num in nums[1:]:
5            prefix.append(prefix[-1] * num)
6        
7        suffix = [nums[-1]]
8        for j in range(len(nums) - 2, -1, -1):
9            suffix.append(suffix[-1] * nums[j])
10        suffix = suffix[::-1]
11
12        answer = [0] * len(nums)
13
14        for i in range(len(nums)):
15            left = prefix[i - 1] if i - 1 >= 0 else 1
16            right = suffix[i + 1] if i + 1 < len(nums) else 1
17            answer[i] = left * right
18        
19        return answer
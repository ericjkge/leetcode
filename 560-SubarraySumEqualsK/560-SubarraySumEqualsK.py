# Last updated: 6/14/2026, 10:31:00 AM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix = [0]
4
5        for i in range(len(nums)):
6            prefix.append(prefix[-1] + nums[i])
7
8        count = 0
9        seen = defaultdict(int)
10        
11        for i in range(len(prefix)):
12            target = prefix[i] - k
13            if target in seen:
14                count += seen[target]
15            seen[prefix[i]] += 1
16
17        return count
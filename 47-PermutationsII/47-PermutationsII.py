# Last updated: 9/3/2025, 10:14:41 AM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        seen = set()

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
            
            for i in range(n):
                if i in seen:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in seen:
                    continue
                seen.add(i)
                path.append(nums[i])
                backtrack(path)
                seen.remove(i)
                path.pop()

        backtrack([])
        return ans
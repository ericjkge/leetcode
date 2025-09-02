# Last updated: 9/2/2025, 8:02:14 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def backtrack(index, path):
            ans.append(path[:])

            if len(path) == n:
                return
            
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
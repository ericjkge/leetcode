# Last updated: 9/3/2025, 9:54:28 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        for num in nums:
            backtrack([num])

        return ans
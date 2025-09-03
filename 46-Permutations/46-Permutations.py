# Last updated: 9/3/2025, 10:07:24 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seen = set()

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    path.append(num)
                    backtrack(path)
                    seen.remove(num)
                    path.pop()

        backtrack([])
        return ans
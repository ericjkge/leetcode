# Last updated: 7/20/2025, 9:27:22 PM
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        count = [0] * len(cookies)

        def backtrack(i):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(count))
                return

            if max(count) > ans:
                return
            
            for j in range(k):
                count[j] += cookies[i]
                backtrack(i + 1)
                count[j] -= cookies[i]
        
        backtrack(0)
        return ans
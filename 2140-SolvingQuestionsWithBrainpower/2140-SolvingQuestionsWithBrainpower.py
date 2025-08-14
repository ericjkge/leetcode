# Last updated: 8/14/2025, 4:59:13 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def dp(i):
            if i >= n:
                return 0
            points, brainpower = questions[i]
            return max(dp(i + 1), points + dp(i + brainpower + 1))
        
        return dp(0)
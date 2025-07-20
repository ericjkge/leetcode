# Last updated: 7/21/2025, 12:25:30 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(start, path):
            if start == len(s):
                ans.append(path[:])
                return

            for i in range(start, len(s)):
                if isPalindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans


# Last updated: 7/21/2025, 12:23:17 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

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


# Last updated: 9/4/2025, 11:32:20 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(start, path):
            if start == n:
                ans.append(path[:])
                return
            
            for i in range(start, n):
                if isPalindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    backtrack(i + 1, path)
                    path.pop()
            
        backtrack(0, [])
        return ans
# Last updated: 7/20/2025, 11:58:13 PM
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def is_valid(start, end):
            if end - start + 1 == 1 or (s[start] != "0" and end - start + 1 <= 3 and int(s[start:end + 1]) <= 255):
                return True
            return False 

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return
            
            for end in range(start, len(s)):
                if is_valid(start, end):
                    print(s[start:end + 1])
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return ans
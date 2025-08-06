# Last updated: 8/6/2025, 10:37:40 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0 # min, max open
        for char in s:
            if char == "(":
                lo += 1
                hi += 1
            elif char == ")":
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
        
            if hi < 0:
                return False
            
            lo = max(lo, 0)
        
        return lo == 0
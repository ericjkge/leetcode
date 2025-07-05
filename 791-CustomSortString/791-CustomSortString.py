# Last updated: 7/4/2025, 10:41:51 PM
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        priority = {char:index for index, char in enumerate(order)} # index, char
        string = list(s)
        ans = []

        for char in priority:
            while char in string:
                ans.append(char)
                string.remove(char)
        
        return "".join(ans + string)
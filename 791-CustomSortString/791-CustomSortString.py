# Last updated: 7/4/2025, 10:49:48 PM
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        for char in order:
            if char in count:
                ans.append(char * count[char])
                del count[char]
        
        for char, freq in count.items():
            ans.append(char * freq)
        
        return "".join(ans)

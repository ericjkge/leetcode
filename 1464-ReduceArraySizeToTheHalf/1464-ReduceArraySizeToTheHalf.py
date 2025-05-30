# Last updated: 5/30/2025, 12:07:29 PM
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr) # num, freq
        n = len(arr)
        counts = [val for key, val in c.most_common()]
    
        ans = removed = 0
        
        for count in counts:
            removed += count
            ans += 1
            if removed >= (n / 2):
                break
        
        return ans
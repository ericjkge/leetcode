# Last updated: 9/4/2025, 1:09:01 PM
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        odd = [ch for ch, count in counter.items() if count % 2 != 0]
        if len(odd) > 1:
            return []
        
        mid = odd[0] if odd else ""
        half = []
        for ch, count in counter.items():
            half.extend([ch] * (count // 2))
        half.sort()

        ans = []
        seen = set()
        n = len(half)

        def backtrack(path):
            if len(path) == n:
                half_str = "".join(path)
                ans.append(half_str + mid + half_str[::-1])
                return
            
            for i in range(n):
                if i in seen:
                    continue
                if i > 0 and half[i] == half[i - 1] and i - 1 not in seen:
                    continue
                seen.add(i)
                path.append(half[i])
                backtrack(path)
                seen.remove(i)
                path.pop()
        
        backtrack([])
        return ans
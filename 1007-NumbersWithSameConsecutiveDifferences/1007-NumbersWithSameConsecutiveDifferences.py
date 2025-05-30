# Last updated: 5/30/2025, 12:07:42 PM
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr):
            if len(curr) == n:
                ans.append(int("".join(map(str, curr))))
                return
            
            for i in range(10):
                if len(curr) == 0:
                    if i == 0:
                        continue
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
                else:
                    if abs(i - curr[-1]) == k:
                        curr.append(i)
                        backtrack(curr)
                        curr.pop()

        ans = []
        backtrack([])
        return ans
# Last updated: 7/9/2025, 12:56:56 AM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = -1
        trusts = defaultdict(list)
        trusted_by = defaultdict(list)
        for a, b in trust:
            trusts[a].append(b)
            trusted_by[b].append(a)
        

        for i in range(1, n + 1):
            if not trusts[i] and len(trusted_by[i]) == n - 1:
                ans = i

        return ans
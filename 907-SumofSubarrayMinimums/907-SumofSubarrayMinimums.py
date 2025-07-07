# Last updated: 7/7/2025, 2:45:07 PM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)

        # PLE
        ple = [0] * n
        stack = []
        for i in range(n):
            counter = 1
            while stack and stack[-1][0] > arr[i]:
                counter += stack.pop()[1]
            ple[i] = counter
            stack.append((arr[i], counter))

        # NLE
        nle = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            counter = 1
            while stack and stack[-1][0] >= arr[i]:
                counter += stack.pop()[1]
            nle[i] = counter
            stack.append((arr[i], counter))
        
        ans = 0
        for i in range(n):
            ans = (ans + ple[i] * nle[i] * arr[i]) % MOD
        return ans